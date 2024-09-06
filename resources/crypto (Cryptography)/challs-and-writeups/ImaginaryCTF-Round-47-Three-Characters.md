# Three Characters
This challenge is a 75 point Web challenge from Round 47 of Imaginary CTF. We get the following source file:

```go
package main
  
import (
        "crypto/sha1"
        _ "embed"
        "encoding/json"
        "fmt"
        "log"
        "math/rand"
        "net/http"
        "os"
        "time"
)
  
//go:embed main.go
var source []byte
  
//go:embed Dockerfile
var docker []byte
  
var password string
  
var passwordLength = 32
var passwordNumber = 0
  
var hashes = make(map[string]string)
var letters = []byte("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
var keyPattern = "%d-%d-%d"
  
type charactersResponse struct {
        Indices []int  `json:"indices"`
        Hash    string `json:"hash"`
        Number  int    `json:"number"`
}
  
func randStringBytes(n int) string {
  
        b := make([]byte, n)
        for i := range b {
                b[i] = letters[rand.Intn(len(letters))]
        }
        return string(b)
}
  
func updatePassword() {
        password = randStringBytes(passwordLength)
  
        log.Printf("Password is %s", password)
  
        tempHashes := make(map[string]string)
  
        for i := 0; i < passwordLength; i++ {
                for j := 0; j < passwordLength; j++ {
                        for k := 0; k < passwordLength; k++ {
                                key := fmt.Sprintf(keyPattern, i, j, k)
                                hash := fmt.Sprintf("%x", sha1.Sum([]byte{password[i], password[j], password[k]}))
                                tempHashes[key] = hash
                        }
                }
        }
  
        hashes = tempHashes
        passwordNumber += 1
}
  
func indexHandler(w http.ResponseWriter, r *http.Request) {
        http.ServeFile(w, r, "index.html")
}
  
func sourceHandler(w http.ResponseWriter, r *http.Request) {
        w.Write(source)
}
  
func dockerHandler(w http.ResponseWriter, r *http.Request) {
        w.Write(docker)
}

func passwordHandler(w http.ResponseWriter, r *http.Request) {
        err := r.ParseForm()
        if err != nil {
                w.WriteHeader(http.StatusBadRequest)
                w.Write([]byte("Failed to parse request"))
                return
        }
  
        if !r.Form.Has("password") {
                w.WriteHeader(http.StatusBadRequest)
                w.Write([]byte("No password submitted"))
                return
        }
  
        if r.Form.Get("password") == password {
                fmt.Fprintf(w, "Flag: %s", os.Getenv("FLAG"))
                return
        }
  
        w.WriteHeader(http.StatusForbidden)
        w.Write([]byte("Incorrect password"))
}
  
func charactersHandler(w http.ResponseWriter, r *http.Request) {
        indicies := []intrand.Intn(passwordLength), rand.Intn(passwordLength), rand.Intn(passwordLength)}
        hash:= hashes[fmt.Sprintf(keyPattern, indicies[0], indicies[1], indicies[2])]
  
        w.Header().Set("Content-Type", "application/json")
        json.NewEncoder(w).Encode(&charactersResponse{Indices: indicies, Hash: hash, Number: passwordNumber})
}
  
func main() {
        updatePassword()
  
        http.HandleFunc("/", indexHandler)
        http.HandleFunc("/source", sourceHandler)
        http.HandleFunc("/docker", dockerHandler)
        http.HandleFunc("/password", passwordHandler)
        http.HandleFunc("/characters", charactersHandler)
  
        reset, _ := time.ParseDuration(os.Getenv("RESET_TIME"))
        ticker := time.NewTicker(reset)
  
        go func() {
                for range ticker.C {
                        updatePassword()
                }
        }()
  
        log.Fatal(http.ListenAndServe(":8080", nil))
}
```

We have 2 endpoints that we really care about:
- `/password`: Where we submit the password
- `/characters`: Where we can get the hash of three random characters in the password

Our goal will be to submit the password to the `/password` endpoint. We also know that the password is 32 chars, and can be any lower or upper case letter. The `/characters` endpoint acts as an oracle, giving us some information about 3 random indices in the password. This is what a GET request to `/characters` looks like:
```json
{
	"indices": [
		16,
		27,
		15
	],
	"hash": "5fe8cc5d93537703383b11dbd3db63853cac9298",
	"number": 186447
}
```

Consulting the `updatePassword` function, it looks like this endpoint returns the result of taking the indices listed, combining like this: `{val at index 1}-{val at index 2}-{val at index 3}`, then running a SHA1sum on it. We can use this knowledge to precompute a list of all possible hashes using these rules:
```python
password_len = 32

hashes_map = {}

possible_chadrs = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
for char_i in possible_chars:
    for char_j in possible_chars:
	    for char_k in possible_chars:
			val = f"{char_i}{char_j}{char_k}"
			key = hashlib.sha1(val.encode()).hexdigest()
			hashes_map[key] = val
```

We can then use this precomputed list in combination with the information we get from the `/characters` endpoint to learn the value at 3 indices in the password string. For example if we take the result from `/characters` above, we know that the hash `5fe8cc5d93537703383b11dbd3db63853cac9298` is the SHA1sum of the values at the 16th, 27th, and 15th index, combined like this `{password[16]}-{password[27]}-{password[15]}`. We can look up the hash in the precomputed dictionary to find that the value is `Ock`, meaning the original string was `O-c-k`. Now we know 3 of the letters of the password. Let's build a quick script to automate this, then send it to the `/password` endpoint:

```python
while True:
    r = requests.get("https://three.ictf.iciaran.com/characters")
    data = json.loads(r.text)
    chars = hashes_map[data['hash']]
    indices = data['indices']
  
    for pair in zip(indices, chars):
        known_password_chars[pair[0]] = pair[1]

    if all([char != '-' for char in known_password_chars]):
        break
    print(''.join(known_password_chars))
  
print(f"Password is {''.join(known_password_chars)}")
print(f"Authenticating with password")
  
data = {
    "password": ''.join(known_password_chars)
}

r = requests.post('https://three.ictf.iciaran.com/password', data=data)
print(r.text)
```

It looks like the password frequently changes, so it takes a few tries, but the final result is:
```
> python3 hashes.py                                         
------------------C----------Vd-                            
-------z--f--s----C----------Vd-                            
-------z--fF-s---BC----------Vd-                            
-------z--fF-s---BC--P-------VdS                            
-------z-qfFIs---BC--P----u--VdS                           
---w---z-qfFIs---BC--P----u-EVdS                            
---wc--z-qfFIsY--BC--P--v-u-EVdS                            
---wc--z-qfFIsY-mBC--P--v-u-EVdS                            
---wc--zJqfFIsY-mBC--P--v-u-EVdS                            
-Y-wc--zJqfFIsY-mBC--P--v-u-EVdS                            
-YKwc--zJqfFIsY-mBC--P--v-u-EVdS                            
-YKwc--zJqfFIsY-mBC--P--v-u-EVdS                            
-YKwc--zJqfFIsY-mBC--P--v-u-EVdS                            
-YKwc--zJqfFIsY-mBC--P--v-u-EVdS                            
-YKwc--zJqfFIsY-mBC--Po-v-u-EVdS                           
gYKwc--zJqfFIsY-mBC--Po-v-u-EVdS                            
gYKwc--zJqfFIsY-mBC-fPo-v-u-EVdS                            
gYKwc--zJqfFIsY-mBC-fPo-v-u-EVdS                            
gYKwc--zJqfFIsY-mBC-fPonv-u-EVdS                            
gYKwc--zJqfFIsY-mBC-fPonv-u-EVdS                            
gYKwc--zJqfFIsY-mBC-fPonv-u-EVdS                            
gYKwc--zJqfFIsY-mBC-fPonv-u-EVdS                            
gYKwc--zJqfFIsY-mBCrfPonv-u-EVdS                            
gYKwc--zJqfFIsY-mBCrfPonv-u-EVdS                            
gYKwc--zJqfFIsY-mBCrfPonv-u-EVdS                            
gYKwc-ezJqfFIsY-mBCrfPonv-u-EVdS                            
gYKwc-ezJqfFIsY-mBCrfPonv-u-EVdS                            
gYKwc-ezJqfFIsY-mBCrfPonv-u-EVdS                            
gYKwc-ezJqfFIsY-mBCrfPonv-u-EVdS                            
gYKwc-ezJqfFIsY-mBCrfPonv-uUEVdS                            
gYKwc-ezJqfFIsY-mBCrfPonv-uUEVdS                            
gYKwc-ezJqfFIsY-mBCrfPonv-uUEVdS                            
gYKwc-ezJqfFIsY-mBCrfPonv-uUEVdS                            
gYKwc-ezJqfFIsY-mBCrfPonv-uUEVdS                            
gYKwc-ezJqfFIsY-mBCrfPonvEuUEVdS                            
gYKwc-ezJqfFIsY-mBCrfPonvEuUEVdS                            
gYKwc-ezJqfFIsY-mBCrfPonvEuUEVdS                            
gYKwc-ezJqfFIsY-mBCrfPonvEuUEVdS                            
gYKwc-ezJqfFIsY-mBCrfPonvEuUEVdS                            
gYKwc-ezJqfFIsY-mBCrfPonvEuUEVdS                            
gYKwc-ezJqfFIsY-mBCrfPonvEuUEVdS                            
gYKwc-ezJqfFIsY-mBCrfPonvEuUEVdS                            
gYKwc-ezJqfFIsY-mBCrfPonvEuUEVdS                            
gYKwc-ezJqfFIsY-mBCrfPonvEuUEVdS                            
gYKwc-ezJqfFIsYomBCrfPonvEuUEVdS                            
Password is gYKwcKezJqfFIsYomBCrfPonvEuUEVdS                
Authenticating with password                                
Flag: ictf{00ps_th1s_1s_jus7_l0ts_0f_thr33_l3tt3r_p4ssw0rds}
```

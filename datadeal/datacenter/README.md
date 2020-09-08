# API

## retrieve api
<span style="border-bottom:2px dashed blue;">
The following use retrieve api to reduce resources.

**retrieve** field : place your action here.

**data**     field : place request data here.
</span>

```
POST - https://vk4uikzpgc.execute-api.ap-east-1.amazonaws.com/dev/rpc
rpc: for admin use.

POST - https://vk4uikzpgc.execute-api.ap-east-1.amazonaws.com/dev/retrieve
retrieve: for app use.

wss://3x9r4af6h6.execute-api.ap-east-1.amazonaws.com/dev
wss: for app use


POST - https://vk4uikzpgc.execute-api.ap-east-1.amazonaws.com/dev/rpc
POST - https://vk4uikzpgc.execute-api.ap-east-1.amazonaws.com/dev/retrieve
GET - https://vk4uikzpgc.execute-api.ap-east-1.amazonaws.com/dev/get_captcha
GET - https://vk4uikzpgc.execute-api.ap-east-1.amazonaws.com/dev/get_captcha_example
GET - https://vk4uikzpgc.execute-api.ap-east-1.amazonaws.com/dev/get_captcha/png
POST - https://vk4uikzpgc.execute-api.ap-east-1.amazonaws.com/dev/verify_captcha
GET - https://vk4uikzpgc.execute-api.ap-east-1.amazonaws.com/dev/quotes
wss://3x9r4af6h6.execute-api.ap-east-1.amazonaws.com/dev

商户中心
//The following wss url is for no sign but login_by_google_code of new admins' usage
wss://qwymti9uo3.execute-api.ap-east-1.amazonaws.com/dev
https://g0trgjx7cg.execute-api.ap-east-1.amazonaws.com/dev/rpc
```
### prd
```
  POST - https://bv8nlzm0uh.execute-api.ap-southeast-1.amazonaws.com/prd/rpc
  POST - https://bv8nlzm0uh.execute-api.ap-southeast-1.amazonaws.com/prd/retrieve
  GET - https://bv8nlzm0uh.execute-api.ap-southeast-1.amazonaws.com/prd/get_captcha
  GET - https://bv8nlzm0uh.execute-api.ap-southeast-1.amazonaws.com/prd/get_captcha_example
  GET - https://bv8nlzm0uh.execute-api.ap-southeast-1.amazonaws.com/prd/get_captcha/png
  POST - https://bv8nlzm0uh.execute-api.ap-southeast-1.amazonaws.com/prd/verify_captcha
  GET - https://bv8nlzm0uh.execute-api.ap-southeast-1.amazonaws.com/prd/quotes
  POST - https://bv8nlzm0uh.execute-api.ap-southeast-1.amazonaws.com/prd/creditable
  POST - https://bv8nlzm0uh.execute-api.ap-southeast-1.amazonaws.com/prd/feed
  POST - https://bv8nlzm0uh.execute-api.ap-southeast-1.amazonaws.com/prd/readonly
  wss://vfwcqdiyh0.execute-api.ap-southeast-1.amazonaws.com/prd
商户中心地址：
  https://pybpvo2l09.execute-api.ap-southeast-1.amazonaws.com/prd/rpc
  wss://pav8db1756.execute-api.ap-southeast-1.amazonaws.com/prd
```

### 1. register(optional)

  POST - https://vk4uikzpgc.execute-api.ap-east-1.amazonaws.com/dev/retrieve

or: wss://3x9r4af6h6.execute-api.ap-east-1.amazonaws.com/dev

//const  "**retrieve**":"register"
```
type retrieve_request struct {
	Appid     string      `json:"appid"`
	Sign      string      `json:"sign"`
	SignType  string      `json:"sign_type"`
	Retrieve string      `json:"retrieve"`
	Data     interface{} `json:"data"`
	Seq      string      `json:"seq"`
}

type register_req struct {
	NickName  string `json:"nick_name"`
	Name      string `json:"name"`  // optional, but should unique
	Phone     string `json:"phone"`
	PhoneCode string `json:"phone_code"`
	SmsCode   string `json:"sms_code"`
	CaptchaId string `json:"captcha_id"`
	Password  string `json:"password"`
	DeviceId  string `json:"device_id"`
	PublicKey string `json:"public_key"`
	Pushid    string `json:"pushid"`
}

type register_resp struct {
	NickName string `json:"nick_name"`
	Retrieve   string   `json:"retrieve"`
	Seq        string   `json:"seq"`
	Result   int    `json:"result"`
	Comment  string `json:"comment"`
}
```

### 2. login
  
  POST - https://vk4uikzpgc.execute-api.ap-east-1.amazonaws.com/dev/retrieve

or: wss://3x9r4af6h6.execute-api.ap-east-1.amazonaws.com/dev

//const  "**retrieve**":"login"
```
// use phone&phone_code to login. NOT Name !!!
type retrieve_request struct {
	Appid     string      `json:"appid"`
	Sign      string      `json:"sign"`
	SignType  string      `json:"sign_type"`
	Retrieve string      `json:"retrieve"`
	Data     interface{} `json:"data"`
	Seq        string   `json:"seq"`
}

type login_req struct {
	Name      string  `json:"name"`
	Phone      string `json:"phone"`
	PhoneCode  string `json:"phone_code"`
	SmsCode    string `json:"sms_code"`
	Nonce      string `json:"nonce"`
	ClientType string `json:"client_type"`
	CaptchaId  string `json:"captcha_id"`
	Password  string `json:"password"`
}

type login_resp struct {
	NickName    string               `json:"nick_name"`
	UserNo      string               `json:"user_no"`
	Logoid      string               `json:"logoid"`
	Assets      []*iproto.UserAssets `json:"assets"`
	TotalGz     string               `json:"total_gz"` //added
	Token       string               `json:"token"`
	KycStatus   string               `json:"kyc_status"`
	BioEnable   string               `json:"bio_enable"`
	SmsEnable   string               `json:"sms_enable"`
	TwofaEnable string               `json:"twofa_enable"` //DISABLED,ENABLED,BINDED,NOT_BINDED
	Retrieve    string               `json:"retrieve"`
	Seq         string               `json:"seq"`
	Result      reterr.ErrCode       `json:"result"`
	Comment     string               `json:"comment"`
}

type UserAssets struct {
	AssetName string `json:"asset_name"`
	Balance   string `json:"balance"`
	Frozen    string `json:"frozen"`
	Uuid      uint64 `json:"uuid"`
	Address   string `json:"address"`
}

```
### 2.1. login_by_phone_password
  
  POST - https://vk4uikzpgc.execute-api.ap-east-1.amazonaws.com/dev/retrieve

or: wss://3x9r4af6h6.execute-api.ap-east-1.amazonaws.com/dev

//const  "**retrieve**":"login_by_phone_password"
```
type retrieve_request struct {
	Appid     string      `json:"appid"`
	Sign      string      `json:"sign"`
	SignType  string      `json:"sign_type"`
	Retrieve string      `json:"retrieve"`
	Data     interface{} `json:"data"`
	Seq        string   `json:"seq"`
}

type login_req struct {
	Phone      string `json:"phone"`
	PhoneCode  string `json:"phone_code"`
	SmsCode    string `json:"sms_code"` // if first time login
	Nonce      string `json:"nonce"`
	ClientType string `json:"client_type"`
	CaptchaId  string `json:"captcha_id"`
	Password   string `json:"password"`
	DeviceId   string `json:"device_id"` // if not empty&not first time, need sms
}

type login_resp struct {
	NickName string               `json:"nick_name"`
	Logoid   string               `json:"logoid"`
	Assets   []*UserAssets        `json:"assets"`
	TotalGz  string               `json:"total_gz"`
	Token    string               `json:"token"`
	Retrieve   string   		  `json:"retrieve"`
	Seq        string  			  `json:"seq"`
	Result   reterr.ErrCode       `json:"result"`
	Comment  string               `json:"comment"`
}

type UserAssets struct {
	AssetName string `json:"asset_name"`
	Balance   string `json:"balance"`
	Frozen    string `json:"frozen"`
	Uuid      uint64 `json:"uuid"`
	Address   string `json:"address"`
}

```
### 2.2. login_by_userno_password
//const  "**retrieve**":"login_by_userno_password"
### 2.3. login_by_userno_google_code
//const  "**retrieve**":"login_by_userno_google_code"
### 2.4. login_by_phone_google_code
//const  "**retrieve**":"login_by_phone_google_code"
```
type retrieve_request struct {
	Appid     string      `json:"appid"`
	Sign      string      `json:"sign"`
	SignType  string      `json:"sign_type"`
	Retrieve string      `json:"retrieve"`
	Data     interface{} `json:"data"`
	Seq        string   `json:"seq"`
}

type login_req struct {
	Name       string `json:"name"`
	Phone      string `json:"phone"`
	PhoneCode  string `json:"phone_code"`
	Email      string `json:"email"`
	Password   string `json:"password"` // when use email, use this.
	SmsCode    string `json:"sms_code"`
	Nonce      string `json:"nonce"`
	ClientType string `json:"client_type"`
	CaptchaId  string `json:"captcha_id"`
	DeviceId   string `json:"device_id"`
	OpenId     string `json:"open_id"`
	UserNo     string `json:"user_no"`
	PinCode    string `json:"pin_code"`   //optional for auto register
	PublicKey  string `json:"public_key"` //optional for auto register
	Pushid     string `json:"pushid"`     //optional for auto register
	GoogleCode string `json:"google_code"` //required for by_google_code
}

type login_resp struct {
	NickName  string               `json:"nick_name"`
	UserNo    string               `json:"user_no"`
	Logoid    string               `json:"logoid"`
	Assets    []*iproto.UserAssets `json:"assets"`
	TotalGz   string               `json:"total_gz"` //added
	Token     string               `json:"token"`
	KycStatus string               `json:"kyc_status"`
	BioEnable string               `json:"bio_enable"`
	SmsEnable string               `json:"sms_enable"`
	TwofaEnable string             `json:"twofa_enable"`
	Retrieve  string               `json:"retrieve"`
	Seq       string               `json:"seq"`
	Result    reterr.ErrCode       `json:"result"`
	Comment   string               `json:"comment"`
}

type UserAssets struct {
	AssetName string `json:"asset_name"`
	Balance   string `json:"balance"`
	Frozen    string `json:"frozen"`
	Uuid      uint64 `json:"uuid"`
	Address   string `json:"address"`
}

```

### 3. refresh_token
  
  POST - https://vk4uikzpgc.execute-api.ap-east-1.amazonaws.com/dev/retrieve

or: wss://3x9r4af6h6.execute-api.ap-east-1.amazonaws.com/dev

//const  "**retrieve**":"refresh_token"
```
type retrieve_request struct {
	Appid     string      `json:"appid"`
	Sign      string      `json:"sign"`
	SignType  string      `json:"sign_type"`
	Name      string      `json:"name"`
	Phone     string      `json:"phone"`
	PhoneCode string      `json:"phone_code"`
	Token     string      `json:"token"`
	Retrieve   string   `json:"retrieve"`
	Seq        string   `json:"seq"`
	Data      interface{} `json:"data"`
}
type refresh_req struct {
}

type refresh_resp struct {
	AccessToken  string `json:"access_token"`
	RefreshToken string `json:"refresh_token"`
	TokenType    string `json:"token_type"`
	Expires      int    `json:"expires"`
	Retrieve   string   `json:"retrieve"`
	Seq        string   `json:"seq"`
	Result       int    `json:"result"`
	Comment      string `json:"comment"`
}
```

### 4.send_sms

  POST - https://vk4uikzpgc.execute-api.ap-east-1.amazonaws.com/dev/retrieve

or: wss://3x9r4af6h6.execute-api.ap-east-1.amazonaws.com/dev

//const  "**retrieve**":"send_sms"
//test use: "000000" in field sms_code
```
type retrieve_request struct {
	Appid     string      `json:"appid"`
	Sign      string      `json:"sign"`
	SignType  string      `json:"sign_type"`
	Retrieve   string   `json:"retrieve"`
	Seq        string   `json:"seq"`
	Data     interface{} `json:"data"`
}

type send_sms_request struct {
	Usage     int    `json:"usage"` // 0:register, 1:change password, 2:change telephone, 3:transfer, 4:withdraw, 5:frozen, 6:upate device, 7:without password payment, 8:change pincode, 9:Login, 10:deposit,
	11:recv 12:send
	PhoneCode string `json:"phone_code"`
	Phone     string `json:"phone"`
}

type send_sms_response struct {
	Retrieve   string   `json:"retrieve"`
	Seq        string   `json:"seq"`
	Result  int    `json:"result"`
	Comment string `json:"comment"`
}
```
example: POST:

{"retrieve":"send_sms","data":{"phone": "1234567891","phone_code":"852","usage":1}}

### 5.get_captcha

  GET - https://vk4uikzpgc.execute-api.ap-east-1.amazonaws.com/dev/get_captcha

### 6.get_png

  GET - https://vk4uikzpgc.execute-api.ap-east-1.amazonaws.com/dev/get_captcha/png

### 7.verify_captcha

  POST - https://vk4uikzpgc.execute-api.ap-east-1.amazonaws.com/dev/verify_captcha

### 8.get_captcha_example

  GET - https://vk4uikzpgc.execute-api.ap-east-1.amazonaws.com/dev/get_captcha_example
```
description:
1. get_captcha(a scratch of html)
2. get_png(this is implicit, used in scratch of html)
3. verify_captcha(used in scratch of html when submit, used in example)
4. get_captcha_example, an example of captcha

usage:
1. get_captcha
2. place the verify string in captcha_id field (example: "captcha_id=molbq2BkXu5dGhP&captcha=7829")
```


### 9. transfer
  
  POST - https://vk4uikzpgc.execute-api.ap-east-1.amazonaws.com/dev/retrieve

or: wss://3x9r4af6h6.execute-api.ap-east-1.amazonaws.com/dev

//const  "**retrieve**":"transfer"
```
type retrieve_request struct {
	Appid     string      `json:"appid"`
	Sign      string      `json:"sign"`
	SignType  string      `json:"sign_type"`
	Name      string      `json:"name"`
	Phone     string      `json:"phone"`
	PhoneCode string      `json:"phone_code"`
	Token     string      `json:"token"`
	Retrieve   string   `json:"retrieve"`
	Seq        string   `json:"seq"`
	Data      interface{} `json:"data"`
}
type transfer_req struct {
	AssetName   string `json:"asset_name"`
	OrderId     string `json:"order_id"` //third party order id for reference.
	ToPhone     string `json:"to_phone"`
	ToPhoneCode string `json:"to_phone_code"`
	ToUser      string `json:"to_user"`
	Amount      string `json:"amount"`
	PinCode     string `json:"pin_code"`
}

type transfer_resp struct {
	OrderId     string `json:"order_id"`
	AssetName   string `json:"asset_name"`
	ToPhone     string `json:"to_phone"`
	ToPhoneCode string `json:"to_phone_code"`
	ToUser      string `json:"to_user"`
	Amount      string `json:"amount"`
	Retrieve   string   `json:"retrieve"`
	Seq        string   `json:"seq"`
	Result      int    `json:"result"`
	Comment     string `json:"comment"`
}
```

### **10.assets**
  
  POST - https://vk4uikzpgc.execute-api.ap-east-1.amazonaws.com/dev/retrieve

or: wss://3x9r4af6h6.execute-api.ap-east-1.amazonaws.com/dev

//const  "**retrieve**":"assets_list"
```
type retrieve_request struct {
	Appid     string      `json:"appid"`
	Sign      string      `json:"sign"`
	SignType  string      `json:"sign_type"`
	Name      string      `json:"name"`
	Phone     string      `json:"phone"`
	PhoneCode string      `json:"phone_code"`
	Token     string      `json:"token"`
	Retrieve   string   `json:"retrieve"`
	Seq        string   `json:"seq"`
	Data      interface{} `json:"data"`
}
type assets_req struct {
}

type assets_resp struct {
	Assets  []*iproto.UserAssets `json:"assets"`
	Retrieve   string   `json:"retrieve"`
	Seq        string   `json:"seq"`
	Result  int                  `json:"result"`
	Comment string               `json:"comment"`
}
```


###  11.deposit 

  POST - https://vk4uikzpgc.execute-api.ap-east-1.amazonaws.com/dev/retrieve

or: wss://3x9r4af6h6.execute-api.ap-east-1.amazonaws.com/dev

//const  "**retrieve**":"deposit"
```
type retrieve_request struct {
	Appid     string      `json:"appid"`
	Sign      string      `json:"sign"`
	SignType  string      `json:"sign_type"`
	Name      string      `json:"name"`
	Phone     string      `json:"phone"`
	PhoneCode string      `json:"phone_code"`
	Token     string      `json:"token"`
	Retrieve   string   `json:"retrieve"`
	Seq        string   `json:"seq"`
	Data      interface{} `json:"data"`
}
type deposit_request struct {
	AssetName string `json:"asset_name"`
	From      string `json:"from"` // on chain address
	To        string `json:"to"`   // on chain address
	Amount    string `json:"amount"`
}

type deposit_response struct {
	Retrieve   string   `json:"retrieve"`
	Seq        string   `json:"seq"`
	Result  int    `json:"result"`
	Comment string `json:"comment"`
}
```
###  12.withdraw 

  POST - https://vk4uikzpgc.execute-api.ap-east-1.amazonaws.com/dev/retrieve

or: wss://3x9r4af6h6.execute-api.ap-east-1.amazonaws.com/dev

//const  "**retrieve**":"withdraw"
```
type retrieve_request struct {
	Appid     string      `json:"appid"`
	Sign      string      `json:"sign"`
	SignType  string      `json:"sign_type"`
	Name      string      `json:"name"`
	Phone     string      `json:"phone"`
	PhoneCode string      `json:"phone_code"`
	Token     string      `json:"token"`
	Retrieve   string   `json:"retrieve"`
	Seq        string   `json:"seq"`
	Data      interface{} `json:"data"`
}
type withdraw_request struct {
	AssetName string `json:"asset_name"`
	Amount    string `json:"amount"`
	To        string `json:"to"` //withdraw to address
	PinCode   string `json:"pin_code"`
}

type withdraw_response struct {
	Retrieve   string   `json:"retrieve"`
	Seq        string   `json:"seq"`
	Result  int    `json:"result"`
	Comment string `json:"comment"`
}
```
### 13.assets_gen

POST - https://vk4uikzpgc.execute-api.ap-east-1.amazonaws.com/dev/retrieve

or: wss://3x9r4af6h6.execute-api.ap-east-1.amazonaws.com/dev

//const  "**retrieve**":"assets_gen"
```
type retrieve_request struct {
	Appid     string      `json:"appid"`
	Sign      string      `json:"sign"`
	SignType  string      `json:"sign_type"`
	Name      string      `json:"name"`
	Phone     string      `json:"phone"`
	PhoneCode string      `json:"phone_code"`
	Token     string      `json:"token"`
	Retrieve   string   `json:"retrieve"`
	Seq        string   `json:"seq"`
	Data      interface{} `json:"data"`
}
type assets_gen_req struct {
	AssetName string `json:"asset_name"`
}

type assets_gen_resp struct {
	AssetName string `json:"asset_name"`
	Address   string `json:"address"`
	Retrieve   string   `json:"retrieve"`
	Seq        string   `json:"seq"`
	Result    int    `json:"result"`
	Comment   string `json:"comment"`
}
```

### 16. withdraw_list

POST - https://vk4uikzpgc.execute-api.ap-east-1.amazonaws.com/dev/retrieve

or: wss://3x9r4af6h6.execute-api.ap-east-1.amazonaws.com/dev

//const  "**retrieve**":"withdraw_list"
```
type retrieve_request struct {
	Appid     string      `json:"appid"`
	Sign      string      `json:"sign"`
	SignType  string      `json:"sign_type"`
	Name      string      `json:"name"`
	Phone     string      `json:"phone"`
	PhoneCode string      `json:"phone_code"`
	Token     string      `json:"token"`
	Retrieve   string   `json:"retrieve"`
	Seq        string   `json:"seq"`
	Data      interface{} `json:"data"`
}

type withdraws_list_request struct {
	Asset      string `json:"asset"`
	StartTime  int64  `json:"start_time"`
	EndTime    int64  `json:"end_time"`
	PageNumber int64  `json:"page_number"`
}

type withdraws_list_response struct {
	Withdraws  []iproto.Withdraws `json:"withdraw_list"`
	Asset      string             `json:"asset"`
	StartTime  int64              `json:"start_time"`
	EndTime    int64              `json:"end_time"`
	PageNumber int64              `json:"page_number"`
	Total      int64              `json:"total"`
	Retrieve   string             `json:"retrieve"`
	Seq        string             `json:"seq"`
	Result     int                `json:"result"`
	Comment    string             `json:"comment"`
}
```

### 17. deposit_list

POST - https://vk4uikzpgc.execute-api.ap-east-1.amazonaws.com/dev/retrieve

or: wss://3x9r4af6h6.execute-api.ap-east-1.amazonaws.com/dev

//const  "**retrieve**":"deposit_list"
```
type retrieve_request struct {
	Appid     string      `json:"appid"`
	Sign      string      `json:"sign"`
	SignType  string      `json:"sign_type"`
	Name      string      `json:"name"`
	Phone     string      `json:"phone"`
	PhoneCode string      `json:"phone_code"`
	Token     string      `json:"token"`
	Retrieve   string   `json:"retrieve"`
	Seq        string   `json:"seq"`
	Data      interface{} `json:"data"`
}

type deposit_list_request struct {
	StartTime int64 `json:"start_time"`
	EndTime   int64 `json:"end_time"`
}

type deposit_list_response struct {
	Deposits []iproto.Deposits `json:"deposit_list"`
	Retrieve   string   `json:"retrieve"`
	Seq        string   `json:"seq"`
	Result   int               `json:"result"`
	Comment  string            `json:"comment"`
}

```
### 18. send_list

POST - https://vk4uikzpgc.execute-api.ap-east-1.amazonaws.com/dev/retrieve

or: wss://3x9r4af6h6.execute-api.ap-east-1.amazonaws.com/dev

//const  "**retrieve**":"send_list"
```
type retrieve_request struct {
	Appid     string      `json:"appid"`
	Sign      string      `json:"sign"`
	SignType  string      `json:"sign_type"`
	Name      string      `json:"name"`
	Phone     string      `json:"phone"`
	PhoneCode string      `json:"phone_code"`
	Token     string      `json:"token"`
	Retrieve   string   `json:"retrieve"`
	Seq        string   `json:"seq"`
	Data      interface{} `json:"data"`
}

type send_list_request struct {
	Asset      string `json:"asset"`
	StartTime  int64  `json:"start_time"`
	EndTime    int64  `json:"end_time"`
	PageNumber int64  `json:"page_number"`
}

type send_list_response struct {
	SendList   []iproto.Transfer `json:"send_list"`
	Asset      string            `json:"asset"`
	StartTime  int64             `json:"start_time"`
	EndTime    int64             `json:"end_time"`
	PageNumber int64             `json:"page_number"`
	Total      int64             `json:"total"`
	Retrieve   string            `json:"retrieve"`
	Seq        string            `json:"seq"`
	Result     int               `json:"result"`
	Comment    string            `json:"comment"`
}

```
### 19. recv_list

POST - https://vk4uikzpgc.execute-api.ap-east-1.amazonaws.com/dev/retrieve

or: wss://3x9r4af6h6.execute-api.ap-east-1.amazonaws.com/dev

//const  "**retrieve**":"recv_list"
```
type retrieve_request struct {
	Appid     string      `json:"appid"`
	Sign      string      `json:"sign"`
	SignType  string      `json:"sign_type"`
	Name      string      `json:"name"`
	Phone     string      `json:"phone"`
	PhoneCode string      `json:"phone_code"`
	Token     string      `json:"token"`
	Retrieve   string   `json:"retrieve"`
	Seq        string   `json:"seq"`
	Data      interface{} `json:"data"`
}

type recv_list_request struct {
	Asset      string `json:"asset"`
	StartTime  int64  `json:"start_time"`
	EndTime    int64  `json:"end_time"`
	PageNumber int64  `json:"page_number"`
}

type recv_list_response struct {
	RecvList   []iproto.Transfer `json:"recv_list"`
	Asset      string            `json:"asset"`
	StartTime  int64             `json:"start_time"`
	EndTime    int64             `json:"end_time"`
	PageNumber int64             `json:"page_number"`
	Total      int64             `json:"total"`
	Retrieve   string            `json:"retrieve"`
	Seq        string            `json:"seq"`
	Result     int               `json:"result"`
	Comment    string            `json:"comment"`
}

```
### 20. friend_list

POST - https://vk4uikzpgc.execute-api.ap-east-1.amazonaws.com/dev/retrieve

or: wss://3x9r4af6h6.execute-api.ap-east-1.amazonaws.com/dev

//const  "**retrieve**":"friend_list"
```
type retrieve_request struct {
	Appid     string      `json:"appid"`
	Sign      string      `json:"sign"`
	SignType  string      `json:"sign_type"`
	Name      string      `json:"name"`
	Phone     string      `json:"phone"`
	PhoneCode string      `json:"phone_code"`
	Token     string      `json:"token"`
	Retrieve   string   `json:"retrieve"`
	Seq        string   `json:"seq"`
	Data      interface{} `json:"data"`
}

type friends_list_request struct {
}

type friends_list_response struct {
	FriendList []*iproto.Friend `json:"friend_list"`
	RecentlyFriends []*iproto.Friend `json:"recently_friends"`
	Retrieve   string   `json:"retrieve"`
	Seq        string   `json:"seq"`
	Result     int              `json:"result"`
	Comment    string           `json:"comment"`
}

```
### 21. add_friend

POST - https://vk4uikzpgc.execute-api.ap-east-1.amazonaws.com/dev/retrieve

or: wss://3x9r4af6h6.execute-api.ap-east-1.amazonaws.com/dev

//const  "**retrieve**":"add_friend"
```
type retrieve_request struct {
	Appid     string      `json:"appid"`
	Sign      string      `json:"sign"`
	SignType  string      `json:"sign_type"`
	Name      string      `json:"name"`
	Phone     string      `json:"phone"`
	PhoneCode string      `json:"phone_code"`
	Token     string      `json:"token"`
	Retrieve   string   `json:"retrieve"`
	Seq        string   `json:"seq"`
	Data      interface{} `json:"data"`
}

type add_friend_request struct {
	Name        string `json:"name"`   // custom name
	Phone       string `json:"phone"`
	PhoneCode   string `json:"phone_code"`
	Gender      string `json:"gender"`
	HomeAddress string `home_address`
	WorkAddress string `work_address`
	Email       string `json:"email"`
	Company     string `json:"company"`
}

type add_friend_response struct {
	Name        string `json:"name"`
	Phone       string `json:"phone"`
	PhoneCode   string `json:"phone_code"`
	Gender      string `json:"gender"`
	HomeAddress string `home_address`
	WorkAddress string `work_address`
	Email       string `json:"email"`
	Company     string `json:"company"`
	Logoid      string `json:"logoid"`
	Retrieve    string `json:"retrieve"`
	Seq         string `json:"seq"`
	Result      int    `json:"result"`
	Comment     string `json:"comment"`
}

```

### 22. assets_config_list

POST - https://vk4uikzpgc.execute-api.ap-east-1.amazonaws.com/dev/retrieve

or: wss://3x9r4af6h6.execute-api.ap-east-1.amazonaws.com/dev

//const  "**retrieve**":"assets_config_list"
```
type retrieve_request struct {
	Appid     string      `json:"appid"`
	Sign      string      `json:"sign"`
	SignType  string      `json:"sign_type"`
	Name      string      `json:"name"`
	Phone     string      `json:"phone"`
	PhoneCode string      `json:"phone_code"`
	Token     string      `json:"token"`
	Retrieve   string   `json:"retrieve"`
	Seq        string   `json:"seq"`
	Data      interface{} `json:"data"`
}

type assets_config struct {
	Id                   string `json:"id"`
	Name                 string `json:"name"`
	Digits               int32  `json:"digits"`
	Type                 string `json:"type"`
}

type assets_config_list_req struct {
}

type assets_config_list_resp struct {
	AssetsConfig []*assets_config `json:"assets_config"`
	Retrieve   string   `json:"retrieve"`
	Seq        string   `json:"seq"`
}

```

### 23. symbol_list

POST - https://vk4uikzpgc.execute-api.ap-east-1.amazonaws.com/dev/retrieve

or: wss://3x9r4af6h6.execute-api.ap-east-1.amazonaws.com/dev

//const  "**retrieve**":"symbol_list"
```
type retrieve_request struct {
	Appid     string      `json:"appid"`
	Sign      string      `json:"sign"`
	SignType  string      `json:"sign_type"`
	Name      string      `json:"name"`
	Phone     string      `json:"phone"`
	PhoneCode string      `json:"phone_code"`
	Token     string      `json:"token"`
	Retrieve   string   `json:"retrieve"`
	Seq        string   `json:"seq"`
	Data      interface{} `json:"data"`
}

type symbols struct {
	Id                   string `json:"id"`
	Name                 string `json:"name"` 
	BaseCcy              string `json:"base_ccy"`   
	ProfitCcy            string `json:"profit_ccy"`   
	LastPrice            string `json:"last_price"`
	Bid                  string `json:"bid"`
	Ask                  string `json:"ask"`
}
type symbol_list_req struct {
}
type symbol_list_resp struct {
	Symbols []*symbols `json:"symbols"`
	Retrieve   string   `json:"retrieve"`
	Seq        string   `json:"seq"`
}

```

### 24. position_list

POST - https://vk4uikzpgc.execute-api.ap-east-1.amazonaws.com/dev/retrieve

or: wss://3x9r4af6h6.execute-api.ap-east-1.amazonaws.com/dev

//const  "**retrieve**":"position_list"
```
type retrieve_request struct {
	Appid     string      `json:"appid"`
	Sign      string      `json:"sign"`
	SignType  string      `json:"sign_type"`
	Name      string      `json:"name"`
	Phone     string      `json:"phone"`
	PhoneCode string      `json:"phone_code"`
	Token     string      `json:"token"`
	Retrieve   string   `json:"retrieve"`
	Seq        string   `json:"seq"`
	Data      interface{} `json:"data"`
}

type iPositions struct {
	Id                   string   `json:"id"`
	Vid                  uint64   `json:"vid"`
	Symbol               string   `json:"symbol"`
	BaseAsset            string   `json:"base_asset"`
	BaseAmount           string   `json:"base_amount"`
	ProfitAsset          string   `json:"profit_asset"`
	ProfitAmount         string   `json:"profit_amount"`
	User                 string   `json:"user"`
}
type positions_req struct {
}

type positions_resp struct {
	Positions []*iPositions       `json:"positions"`
	Retrieve   string   `json:"retrieve"`
	Seq        string   `json:"seq"`
	Result    int                 `json:"result"`
	Comment   string              `json:"comment"`
}

```

### 25. add_base

POST - https://vk4uikzpgc.execute-api.ap-east-1.amazonaws.com/dev/retrieve

or: wss://3x9r4af6h6.execute-api.ap-east-1.amazonaws.com/dev

//const  "**retrieve**":"add_base"
```
type retrieve_request struct {
	Appid     string      `json:"appid"`
	Sign      string      `json:"sign"`
	SignType  string      `json:"sign_type"`
	Name      string      `json:"name"`
	Phone     string      `json:"phone"`
	PhoneCode string      `json:"phone_code"`
	Token     string      `json:"token"`
	Retrieve   string   `json:"retrieve"`
	Seq        string   `json:"seq"`
	Data      interface{} `json:"data"`
}
type add_base_req struct {
	AssetName string `json:"asset_name"`
	Amount    string `json:"amount"`
	Symbol    string `json:"symbol"`
	Price     string `json:"price"`
	Nonce     string `json:"nonce"`
}

type add_base_resp struct {
	DealId       string `json:"deal_id"`
	Symbol       string `json:"symbol"`
	AddAssetName string `json:"add_asset_name"`
	AddAmount    string `json:"add_amount"`
	Retrieve   string   `json:"retrieve"`
	Seq        string   `json:"seq"`
	Result       int    `json:"result"`
	Comment      string `json:"comment"`
}

```
### 26. sub_base

POST - https://vk4uikzpgc.execute-api.ap-east-1.amazonaws.com/dev/retrieve

or: wss://3x9r4af6h6.execute-api.ap-east-1.amazonaws.com/dev

//const  "**retrieve**":"sub_base"
```
type retrieve_request struct {
	Appid     string      `json:"appid"`
	Sign      string      `json:"sign"`
	SignType  string      `json:"sign_type"`
	Name      string      `json:"name"`
	Phone     string      `json:"phone"`
	PhoneCode string      `json:"phone_code"`
	Token     string      `json:"token"`
	Retrieve   string   `json:"retrieve"`
	Seq        string   `json:"seq"`
	Data      interface{} `json:"data"`
}
type sub_base_req struct {
	AssetName string `json:"asset_name"`
	Amount    string `json:"amount"`
	Symbol    string `json:"symbol"`
	Price     string `json:"price"`
	Nonce     string `json:"nonce"`
}

type sub_base_resp struct {
	DealId       string `json:"deal_id"`
	Symbol       string `json:"symbol"`
	AddAssetName string `json:"add_asset_name"`
	AddAmount    string `json:"add_amount"`
	Retrieve   string   `json:"retrieve"`
	Seq        string   `json:"seq"`
	Result       int    `json:"result"`
	Comment      string `json:"comment"`
}

```

### 27. add_profit

POST - https://vk4uikzpgc.execute-api.ap-east-1.amazonaws.com/dev/retrieve

or: wss://3x9r4af6h6.execute-api.ap-east-1.amazonaws.com/dev

//const  "**retrieve**":"add_profit"
```
type retrieve_request struct {
	Appid     string      `json:"appid"`
	Sign      string      `json:"sign"`
	SignType  string      `json:"sign_type"`
	Name      string      `json:"name"`
	Phone     string      `json:"phone"`
	PhoneCode string      `json:"phone_code"`
	Token     string      `json:"token"`
	Retrieve   string   `json:"retrieve"`
	Seq        string   `json:"seq"`
	Data      interface{} `json:"data"`
}

type add_profit_req struct {
	AssetName string `json:"asset_name"`
	Amount    string `json:"amount"`
	Symbol    string `json:"symbol"`
	Price     string `json:"price"`
	Nonce     string `json:"nonce"`
}

type add_profit_resp struct {
	DealId       string `json:"deal_id"`
	Symbol       string `json:"symbol"`
	AddAssetName string `json:"add_asset_name"`
	AddAmount    string `json:"add_amount"`
	Retrieve   string   `json:"retrieve"`
	Seq        string   `json:"seq"`
	Result       int    `json:"result"`
	Comment      string `json:"comment"`
}

```
### 28. sub_profit

POST - https://vk4uikzpgc.execute-api.ap-east-1.amazonaws.com/dev/retrieve

or: wss://3x9r4af6h6.execute-api.ap-east-1.amazonaws.com/dev
//const  "**retrieve**":"sub_profit"
```
type retrieve_request struct {
	Appid     string      `json:"appid"`
	Sign      string      `json:"sign"`
	SignType  string      `json:"sign_type"`
	Name      string      `json:"name"`
	Phone     string      `json:"phone"`
	PhoneCode string      `json:"phone_code"`
	Token     string      `json:"token"`
	Retrieve   string   `json:"retrieve"`
	Seq        string   `json:"seq"`
	Data      interface{} `json:"data"`
}

type sub_profit_req struct {
	AssetName string `json:"asset_name"`
	Amount    string `json:"amount"`
	Symbol    string `json:"symbol"`
	Price     string `json:"price"`
	Nonce     string `json:"nonce"`
}

type sub_profit_resp struct {
	DealId       string `json:"deal_id"`
	Symbol       string `json:"symbol"`
	AddAssetName string `json:"add_asset_name"`
	AddAmount    string `json:"add_amount"`
	Retrieve   string   `json:"retrieve"`
	Seq        string   `json:"seq"`
	Result       int    `json:"result"`
	Comment      string `json:"comment"`
}

```

## wss
### 29. subscribe
POST - https://vk4uikzpgc.execute-api.ap-east-1.amazonaws.com/dev/retrieve

or: wss://3x9r4af6h6.execute-api.ap-east-1.amazonaws.com/dev

//const  "**retrieve**":"subscribe"
```
type retrieve_request struct {
	Appid     string      `json:"appid"`
	Sign      string      `json:"sign"`
	SignType  string      `json:"sign_type"`
	Name      string      `json:"name"`
	Phone     string      `json:"phone"`
	PhoneCode string      `json:"phone_code"`
	Token     string      `json:"token"`
	Retrieve   string   `json:"retrieve"`
	Seq        string   `json:"seq"`
	Data      interface{} `json:"data"`
}
type subscribe_request struct {
	Symbol string `json:"symbol"`
}

type subscribe_response struct {
	Symbols []string `json:"symbols"`
	Retrieve   string   `json:"retrieve"`
	Seq        string   `json:"seq"`
	Result  int      `json:"result"`
	Comment string   `json:"comment"`
}
```
### 30. unsubscribe
POST - https://vk4uikzpgc.execute-api.ap-east-1.amazonaws.com/dev/retrieve

or: wss://3x9r4af6h6.execute-api.ap-east-1.amazonaws.com/dev

//const  "**retrieve**":"unsubscribe"
```
type retrieve_request struct {
	Appid     string      `json:"appid"`
	Sign      string      `json:"sign"`
	SignType  string      `json:"sign_type"`
	Name      string      `json:"name"`
	Phone     string      `json:"phone"`
	PhoneCode string      `json:"phone_code"`
	Token     string      `json:"token"`
	Retrieve   string   `json:"retrieve"`
	Seq        string   `json:"seq"`
	Data      interface{} `json:"data"`
}
type unsubscribe_request struct {
	Symbol string `json:"symbol"`
}

type unsubscribe_response struct {
	Symbols []string `json:"symbols"`
	Retrieve   string   `json:"retrieve"`
	Seq        string   `json:"seq"`
	Result  int      `json:"result"`
	Comment string   `json:"comment"`
}
```
### 31. replace_subscribes
POST - https://vk4uikzpgc.execute-api.ap-east-1.amazonaws.com/dev/retrieve

or: wss://3x9r4af6h6.execute-api.ap-east-1.amazonaws.com/dev

//const  "**retrieve**":"replace_subscribes"
```
type retrieve_request struct {
	Appid     string      `json:"appid"`
	Sign      string      `json:"sign"`
	SignType  string      `json:"sign_type"`
	Name      string      `json:"name"`
	Phone     string      `json:"phone"`
	PhoneCode string      `json:"phone_code"`
	Token     string      `json:"token"`
	Retrieve   string   `json:"retrieve"`
	Seq        string   `json:"seq"`
	Data      interface{} `json:"data"`
}
type replace_subscribes_request struct {
	Symbols []string `json:"symbols"`
}

type replace_subscribes_response struct {
	Symbols []string `json:"symbols"`
	Retrieve   string   `json:"retrieve"`
	Seq        string   `json:"seq"`
	Result  int      `json:"result"`
	Comment string   `json:"comment"`
}
```
### 32. market price

wss://3x9r4af6h6.execute-api.ap-east-1.amazonaws.com/dev
```
//response:
type MarketPrice struct {
	Symbol     string   `json:"symbol"`
	LastPrice  string   `json:"last_price"`
	High       string   `json:"high"`
	Low        string   `json:"low"`
	Open       string   `json:"open"`
	PreClose   string   `json:"close"`
	UpdateTime string   `json:"update_time"`
	Bid        []string `json:"bid"`
	Ask        []string `json:"ask"`
	BidVol     []string `json:"bid_vol"`
	AskVol     []string `json:"ask_vol"`
}

```
### 33. last price

wss://3x9r4af6h6.execute-api.ap-east-1.amazonaws.com/dev
```
//response:
type LastPrice struct {
	Symbol     string   `json:"symbol"`
	LastPrice  string   `json:"last_price"`
}

```
### 34. snapshot
// **under modify**

POST - https://vk4uikzpgc.execute-api.ap-east-1.amazonaws.com/dev/retrieve

or wss://3x9r4af6h6.execute-api.ap-east-1.amazonaws.com/dev

// this triggers publish

//const  "**retrieve**":"snapshot"
```
type retrieve_request struct {
	Appid     string      `json:"appid"`
	Sign      string      `json:"sign"`
	SignType  string      `json:"sign_type"`
	Phone     string      `json:"phone"`
	PhoneCode string      `json:"phone_code"`
	Token     string      `json:"token"`
	Retrieve   string   `json:"retrieve"`
	Seq        string   `json:"seq"`
	Data      interface{} `json:"data"`
}
type snapshot_request struct {
}
//response:
type SnapshotPrice struct {
	Symbol     string   `json:"symbol"`
	LastPrice  string   `json:"last_price"`
	High       string   `json:"high"`
	Low        string   `json:"low"`
	Open       string   `json:"open"`
	PreClose   string   `json:"close"`
	UpdateTime string   `json:"update_time"`
	Bid        []string `json:"bid"`
	Ask        []string `json:"ask"`
	BidVol     []string `json:"bid_vol"`
	AskVol     []string `json:"ask_vol"`
}
```
### 35 kyc upload
```
//const  "**retrieve**":"upload"
type retrieve_request struct {
	Appid     string      `json:"appid"`
	Sign      string      `json:"sign"`
	SignType  string      `json:"sign_type"`
	Name      string      `json:"name"`
	Phone     string      `json:"phone"`
	PhoneCode string      `json:"phone_code"`
	Token     string      `json:"token"`
	Retrieve   string   `json:"retrieve"`
	Seq        string   `json:"seq"`
	Data      interface{} `json:"data"`
}
//key:
"TYPE_KYC_UPLOAD_ID",
"TYPE_KYC_UPLOAD_SELFIE",
"TYPE_KYC_UPLOAD_ADDRESS",

type upload_request struct {
	Key      string `json:"key"`
	Body     string `json:"body"`
	Format   string `json:"format"`
	FileName string `json:"file_name"`
}

type upload_response struct {
	FileId   string `json:"fileid"`
	Retrieve string `json:"retrieve"`
	Seq      string `json:"seq"`
	Result   int    `json:"result"`
	Comment  string `json:"comment"`
}

```
### 36 submit kyc
```
//const  "**retrieve**":"submit_kyc"
type retrieve_request struct {
	Appid     string      `json:"appid"`
	Sign      string      `json:"sign"`
	SignType  string      `json:"sign_type"`
	Name      string      `json:"name"`
	Phone     string      `json:"phone"`
	PhoneCode string      `json:"phone_code"`
	Token     string      `json:"token"`
	Retrieve   string   `json:"retrieve"`
	Seq        string   `json:"seq"`
	Data      interface{} `json:"data"`
}

type submit_kyc_request struct {
	RandomNumber              string `json:"random_number"`
	PersonalType              string `json:"personal_type"`
	Portfolio                 string `json:"portfolio"`
	ResidentOf                string `json:"resident_of"`
	Title                     string `json:"title"`
	EnglishFullName           string `json:"english_full_name"`
	ChineseFullName           string `json:"chinese_full_name"`
	IdType                    string `json:"id_type"`
	IdNumber                  string `json:"id_number"`
	Birthday                  string `json:"birthday"`
	Nationality               string `json:"nationality"`
	ContactAddress            string `json:"contact_address"`
	City                      string `json:"city"`
	PostalCode                string `json:"postal_code"`
	CountryOfResidence        string `json:"country_of_residence"`
	Industry                  string `json:"industry"`
	Position                  string `json:"position"`
	YearsWithExistingEmployer string `json:"years_with_existing_employer"`
	AnnualIncome              string `json:"annual_income"`
	IncomeSource              string `json:"income_source"`
	NetAssetValue             string `json:"net_asset_value"`
	IdCardFront               string `json:"id_card_front"`
	IdCardBack                string `json:"id_card_back"`
	ProofOfAddress            string `json:"proof_of_address"`
	Selfie                    string `json:"selfie"`
	TermsConditions           string `json:"terms_conditions"`
	HowYouKnow                string `json:"how_you_know"`
	HowYouKnowOption          string `json:"how_you_know_option"`
	ReasonOpenAccount         string `json:"reason_open_account"`
	ReasonOpenAccountOption   string `json:"reason_open_account_option"`
	LaunderingViolation       string `json:"laundering_violation"`
	MoneyFromIllegal          string `json:"money_from_illegal"`
	HighRiskOfLaundering      string `json:"high_risk_of_laundering"`
}

type submit_kyc_response struct {
	Retrieve string `json:"retrieve"`
	Seq      string `json:"seq"`
	Result   int    `json:"result"`
	Comment  string `json:"comment"`
}

```
### 37 kyc status
```
//const  "**retrieve**":"kyc_status"
type retrieve_request struct {
	Appid     string      `json:"appid"`
	Sign      string      `json:"sign"`
	SignType  string      `json:"sign_type"`
	Name      string      `json:"name"`
	Phone     string      `json:"phone"`
	PhoneCode string      `json:"phone_code"`
	Token     string      `json:"token"`
	Retrieve   string   `json:"retrieve"`
	Seq        string   `json:"seq"`
	Data      interface{} `json:"data"`
}

type kyc_status_request struct {
	Detail string `json:"detail"` // empty for status only, "true" or empty
}

type userKyc struct {
	RandomNumber              string `json:"random_number"`
	PersonalType              string `json:"personal_type"`
	Portfolio                 string `json:"portfolio"`
	ResidentOf                string `json:"resident_of"`
	Title                     string `json:"title"`
	EnglishFullName           string `json:"english_full_name"`
	ChineseFullName           string `json:"chinese_full_name"`
	IdType                    string `json:"id_type"`
	IdNumber                  string `json:"id_number"`
	Birthday                  string `json:"birthday"`
	Nationality               string `json:"nationality"`
	ContactAddress            string `json:"contact_address"`
	City                      string `json:"city"`
	PostalCode                string `json:"postal_code"`
	CountryOfResidence        string `json:"country_of_residence"`
	Industry                  string `json:"industry"`
	Position                  string `json:"position"`
	YearsWithExistingEmployer string `json:"years_with_existing_employer"`
	AnnualIncome              string `json:"annual_income"`
	IncomeSource              string `json:"income_source"`
	NetAssetValue             string `json:"net_asset_value"`
	InvestAmount              string `json:"invest_amount"`
	InvestObjectives          string `json:"invest_objectives"`
	InvestHorizon             string `json:"invest_horizon"`
	InvestExperience          string `json:"invest_experience"`
	IdCardFront               string `json:"id_card_front"`
	IdCardBack                string `json:"id_card_back"`
	ProofOfAddress            string `json:"proof_of_address"`
	Selfie                    string `json:"selfie"`
	TermsConditions           string `json:"terms_conditions"`
	HowYouKnow                string `json:"how_you_know"`
	HowYouKnowOption          string `json:"how_you_know_option"`
	ReasonOpenAccount         string `json:"reason_open_account"`
	ReasonOpenAccountOption   string `json:"reason_open_account_option"`
	LaunderingViolation       string `json:"laundering_violation"`
	MoneyFromIllegal          string `json:"money_from_illegal"`
	HighRiskOfLaundering      string `json:"high_risk_of_laundering"`
	Comment        			  string `json:"comment"`
}

type kyc_status_response struct {
	Kyc      *userKyc 		  `json:"kyc",omitempty`
	Status   string           `json:"status"`
	Retrieve string           `json:"retrieve"`
	Seq      string           `json:"seq"`
	Result   int              `json:"result"`
	Comment  string           `json:"comment"`
}
```
### 38 get kyc file
//const  "**retrieve**":"get_upload"
```
type get_upload_request struct {
	Fileid string `json:"fileid"`
}
type get_upload_response struct {
	Fileid string `json:"fileid"`
	Retrieve   string   `json:"retrieve"`
	Seq        string   `json:"seq"`
	Result  int    `json:"result"`
	Comment string `json:"comment"`
}
```
### 39 delete kyc 
//const  "**retrieve**":"delete_kyc"
//under modification
```
type delete_upload_request struct {
}
type delete_upload_response struct {
	Retrieve   string   `json:"retrieve"`
	Seq        string   `json:"seq"`
	Result  int    `json:"result"`
	Comment string `json:"comment"`
}
```
### 40 gz2dgt
```
//const  "**retrieve**":"submit_gz_to_dgt"
type retrieve_request struct {
	Appid     string      `json:"appid"`
	Sign      string      `json:"sign"`
	SignType  string      `json:"sign_type"`
	Name      string      `json:"name"`
	Phone     string      `json:"phone"`
	PhoneCode string      `json:"phone_code"`
	Token     string      `json:"token"`
	Retrieve   string   `json:"retrieve"`
	Seq        string   `json:"seq"`
	Data      interface{} `json:"data"`
}
type gz_to_dgt_request struct {
	GzWallet string `json:"gz_wallet"`
	IdNumber string `json:"id_number"`
	Amount   string `json:"amount"`
	Nonce    string `json:"nonce"` // random unique id
}
type gz_to_dgt_response struct {
	Nonce      string `json:"nonce"` // from request
	ProposalNo string `json:"proposal_no"`
	Retrieve   string   `json:"retrieve"`
	Seq        string   `json:"seq"`
	Result  int      `json:"result"`
	Comment string   `json:"comment"`
}
```
### 41 dgt2gold
```
//const  "**retrieve**":"submit_dgt_to_gold"
type retrieve_request struct {
	Appid     string      `json:"appid"`
	Sign      string      `json:"sign"`
	SignType  string      `json:"sign_type"`
	Name      string      `json:"name"`
	Phone     string      `json:"phone"`
	PhoneCode string      `json:"phone_code"`
	Token     string      `json:"token"`
	Retrieve   string   `json:"retrieve"`
	Seq        string   `json:"seq"`
	Data      interface{} `json:"data"`
}
type dgt_to_gold_request struct {
	GzWallet string `json:"gz_wallet"`
	IdNumber string `json:"id_number"`
	Amount string `json:"amount"`
	Nonce    string `json:"nonce"` // random unique id
}
type dgt_to_gold_response struct {
	Nonce    string `json:"nonce"` // from request
	ProposalNo string `json:"proposal_no"`
	Retrieve   string   `json:"retrieve"`
	Seq        string   `json:"seq"`
	Result  int      `json:"result"`
	Comment string   `json:"comment"`
}
```
### 42 dgt2gz
```
//const  "**retrieve**":"submit_dgt_to_gz"
type retrieve_request struct {
	Appid     string      `json:"appid"`
	Sign      string      `json:"sign"`
	SignType  string      `json:"sign_type"`
	Name      string      `json:"name"`
	Phone     string      `json:"phone"`
	PhoneCode string      `json:"phone_code"`
	Token     string      `json:"token"`
	Retrieve   string   `json:"retrieve"`
	Seq        string   `json:"seq"`
	Data      interface{} `json:"data"`
}
type dgt_to_gz_request struct {
	GzWallet string `json:"gz_wallet"`
	IdNumber string `json:"id_number"`
	Amount string `json:"amount"`
	Nonce    string `json:"nonce"` // random unique id
}
type dgt_to_gz_response struct {
	Nonce    string `json:"nonce"` // from request
	ProposalNo string `json:"proposal_no"`
	Retrieve   string   `json:"retrieve"`
	Seq        string   `json:"seq"`
	Result  int      `json:"result"`
	Comment string   `json:"comment"`
}
```
### 43 mbt proposal status
```
//const  "**retrieve**":"mbt_status"
type retrieve_request struct {
	Appid     string      `json:"appid"`
	Sign      string      `json:"sign"`
	SignType  string      `json:"sign_type"`
	Name      string      `json:"name"`
	Phone     string      `json:"phone"`
	PhoneCode string      `json:"phone_code"`
	Token     string      `json:"token"`
	Retrieve   string   `json:"retrieve"`
	Seq        string   `json:"seq"`
	Data      interface{} `json:"data"`
}
type mbt_status_request struct {
	ProposalNo string `json:"proposal_no"`
}
type mbt_status_response struct {
	ProposalNo string `json:"proposal_no"`
	Status string    `json:"status"`
	Retrieve   string   `json:"retrieve"`
	Seq        string   `json:"seq"`
	Result  int      `json:"result"`
	Comment string   `json:"comment"`
}
```
### 44 mbt proposal list
```
//const  "**retrieve**":"mbt_proposal_list"
type retrieve_request struct {
	Appid     string      `json:"appid"`
	Sign      string      `json:"sign"`
	SignType  string      `json:"sign_type"`
	Name      string      `json:"name"`
	Phone     string      `json:"phone"`
	PhoneCode string      `json:"phone_code"`
	Token     string      `json:"token"`
	Retrieve   string   `json:"retrieve"`
	Seq        string   `json:"seq"`
	Data      interface{} `json:"data"`
}
type mbt_proposal_list_request struct {
	StartTime int64 	 `json:"start_time"` // of create time
	EndTime   int64 	 `json:"end_time"`
}
type MbtProposals struct {
	User     string      `json:"user"`
	Type     string      `json:"type"`
	Gzwallet string      `json:"gzwallet"`
	IdNumber string      `json:"id_number"`
	Amount   string      `json:"amount"`
	Status   string      `json:"status"`
	Operator string      `json:"operator"`
	Manager  string      `json:"manager"`
	UpdateTime string    `json:"update_time"`
	Comment  string      `json:"comment"`
}
type mbt_proposal_list_response struct {
	Proposals []MbtProposals `json:"proposal_list"`
	Retrieve   string   `json:"retrieve"`
	Seq        string   `json:"seq"`
	Result  int      `json:"result"`
	Comment string   `json:"comment"`
}
```
### 45 update pin code
//const  "**retrieve**":"update_pin_code"
```
type retrieve_request struct {
	Appid     string      `json:"appid"`
	Sign      string      `json:"sign"`
	SignType  string      `json:"sign_type"`
	Name      string      `json:"name"`
	Phone     string      `json:"phone"`
	PhoneCode string      `json:"phone_code"`
	Token     string      `json:"token"`
	Retrieve   string   `json:"retrieve"`
	Seq        string   `json:"seq"`
	Data      interface{} `json:"data"`
}
type update_pin_code_req struct {
	OldPinCode string `json:"old_pin_code"`
	NewPinCode string `json:"new_pin_code"`
}

type update_pin_code_resp struct {
	Retrieve   string   `json:"retrieve"`
	Seq        string   `json:"seq"`
	Result  reterr.ErrCode `json:"result"`
	Comment string         `json:"comment"`
}
```
### 46 change pin code
//const  "**retrieve**":"change_pin_code"
```
type retrieve_request struct {
	Appid     string      `json:"appid"`
	Sign      string      `json:"sign"`
	SignType  string      `json:"sign_type"`
	Phone     string      `json:"phone"`
	PhoneCode string      `json:"phone_code"`
	Token     string      `json:"token"`
	Retrieve   string   `json:"retrieve"`
	Seq        string   `json:"seq"`
	Data      interface{} `json:"data"`
}
type change_pin_code_req struct {
	SmsCode    string `json:"sms_code"`
	NewPinCode string `json:"new_pin_code"`
	GoogleCode  string `json:"google_code"`
}

type change_pin_code_resp struct {
	Retrieve   string   `json:"retrieve"`
	Seq        string   `json:"seq"`
	Result  reterr.ErrCode `json:"result"`
	Comment string         `json:"comment"`
}
```
### 47 get user profile
//const "**retrieve**":"get_user_profile"
```
type retrieve_request struct {
	Appid     string      `json:"appid"`
	Sign      string      `json:"sign"`
	SignType  string      `json:"sign_type"`
	Name      string      `json:"name"`
	Phone     string      `json:"phone"`
	PhoneCode string      `json:"phone_code"`
	Token     string      `json:"token"`
	Retrieve   string   `json:"retrieve"`
	Seq        string   `json:"seq"`
	Data      interface{} `json:"data"`
}
type get_user_profile_req struct {
}

type get_user_profile_resp struct {
	NickName      string         `json:"nick_name"`
	Gender        string         `json:"gender"`
	AreaDistricts string         `json:"area_districts"`
	Birthday      string         `json:"birthday"`
	Retrieve   string   `json:"retrieve"`
	Seq        string   `json:"seq"`
	Result        reterr.ErrCode `json:"result"`
	Comment       string         `json:"comment"`
}
```
### 48 update user profile
//const "**retrieve**":"update_user_profile"
```
type retrieve_request struct {
	Appid     string      `json:"appid"`
	Sign      string      `json:"sign"`
	SignType  string      `json:"sign_type"`
	Name      string      `json:"name"`
	Phone     string      `json:"phone"`
	PhoneCode string      `json:"phone_code"`
	Token     string      `json:"token"`
	Retrieve   string   `json:"retrieve"`
	Seq        string   `json:"seq"`
	Data      interface{} `json:"data"`
}
type update_user_profile_req struct {
	NickName      string `json:"nick_name"`
	Gender        string `json:"gender"`
	AreaDistricts string `json:"area_districts"`
	Birthday      string `json:"birthday"`
}

type update_user_profile_resp struct {
	Retrieve   string   `json:"retrieve"`
	Seq        string   `json:"seq"`
	Result  reterr.ErrCode `json:"result"`
	Comment string         `json:"comment"`
}
```

### 50 is pin code set
//const  "**retrieve**":"is_pin_code_set"
```
type retrieve_request struct {
	Appid     string      `json:"appid"`
	Sign      string      `json:"sign"`
	SignType  string      `json:"sign_type"`
	Name      string      `json:"name"`
	Phone     string      `json:"phone"`
	PhoneCode string      `json:"phone_code"`
	Token     string      `json:"token"`
	Retrieve   string   `json:"retrieve"`
	Seq        string   `json:"seq"`
	Data      interface{} `json:"data"`
}
type is_pin_code_set_req struct {
}

type is_pin_code_set_resp struct {
	IsSet   bool           `json:"is_set"`
	IsPasswordSet bool `json:"is_password_set"`
	Retrieve   string   `json:"retrieve"`
	Seq        string   `json:"seq"`
	Result  reterr.ErrCode `json:"result"`
	Comment string         `json:"comment"`
}
```
### 51 fee config list
//const  "**retrieve**":"fee_config_list"
```
type retrieve_request struct {
	Appid     string      `json:"appid"`
	Sign      string      `json:"sign"`
	SignType  string      `json:"sign_type"`
	Name      string      `json:"name"`
	Phone     string      `json:"phone"`
	PhoneCode string      `json:"phone_code"`
	Token     string      `json:"token"`
	Retrieve   string   `json:"retrieve"`
	Seq        string   `json:"seq"`
	Data      interface{} `json:"data"`
}
type fee_config_list_req struct {
}
type FeeConfig struct{
	Type       string   `json:"type"`
	/*
	TYPE_WITHDRAW = 0;
	TYPE_TRANSFER = 1;
	TYPE_PAYMENT  = 2;
	TYPE_MINT     = 3;
	TYPE_BURN     = 4;
	TYPE_REDEEM   = 5;
	*/
	PerMillion string   `json:"per_million"`  // int value
	PerTxFix   string   `json:"per_tx_fix"`
	AssetName  string   `json:"asset_name"`
}
type fee_config_list_response struct {
	FeeConfigs []*FeeConfig `json:"fee_config_list"`
	Retrieve   string   `json:"retrieve"`
	Seq        string   `json:"seq"`
	Result     int                 `json:"result"`
	Comment    string              `json:"comment"`
}
```
### 52 update friend profile
//const  "**retrieve**":"update_friend_profile"
```
type retrieve_request struct {
	Appid     string      `json:"appid"`
	Sign      string      `json:"sign"`
	SignType  string      `json:"sign_type"`
	Name      string      `json:"name"`
	Phone     string      `json:"phone"`
	PhoneCode string      `json:"phone_code"`
	Token     string      `json:"token"`
	Retrieve   string   `json:"retrieve"`
	Seq        string   `json:"seq"`
	Data      interface{} `json:"data"`
}
type update_friend_profile_req struct {
	Name        string `json:"name"`
	Phone       string `json:"phone"`
	PhoneCode   string `json:"phone_code"`
	Gender      string `json:"gender"`
	HomeAddress string `home_address`
	WorkAddress string `work_address`
	Email       string `json:"email"`
	Company     string `json:"company"`
}

type update_friend_profile_response struct {
	Name        string `json:"name"`
	Phone       string `json:"phone"`
	PhoneCode   string `json:"phone_code"`
	Gender      string `json:"gender"`
	HomeAddress string `home_address`
	WorkAddress string `work_address`
	Email       string `json:"email"`
	Company     string `json:"company"`
	Logoid      string `json:"logoid"`
	Retrieve    string `json:"retrieve"`
	Seq         string `json:"seq"`
	Result      int    `json:"result"`
	Comment     string `json:"comment"`
}
```
### 53 logo upload
//const  "**retrieve**":"upload_logo"
```
type retrieve_request struct {
	Appid     string      `json:"appid"`
	Sign      string      `json:"sign"`
	SignType  string      `json:"sign_type"`
	Name      string      `json:"name"`
	Phone     string      `json:"phone"`
	PhoneCode string      `json:"phone_code"`
	Token     string      `json:"token"`
	Retrieve   string   `json:"retrieve"`
	Seq        string   `json:"seq"`
	Data      interface{} `json:"data"`
}
type upload_request struct {
	Key  string `json:"key"`
	Body string `json:"body"`
}

type upload_response struct {
	FileId  string `json:"fileid"`
	Retrieve   string   `json:"retrieve"`
	Seq        string   `json:"seq"`
	Result  int    `json:"result"`
	Comment string `json:"comment"`
}
```
### 54 get logo 
//const  "**retrieve**":"get_logo"
```
type retrieve_request struct {
	Appid     string      `json:"appid"`
	Sign      string      `json:"sign"`
	SignType  string      `json:"sign_type"`
	Name      string      `json:"name"`
	Phone     string      `json:"phone"`
	PhoneCode string      `json:"phone_code"`
	Token     string      `json:"token"`
	Retrieve   string   `json:"retrieve"`
	Seq        string   `json:"seq"`
	Data      interface{} `json:"data"`
}
type get_upload_request struct {
	Fileid string `json:"fileid"`
}
```
### 55 get last price 
//const  "**retrieve**":"last_price"
```
type retrieve_request struct {
	Appid     string      `json:"appid"`
	Sign      string      `json:"sign"`
	SignType  string      `json:"sign_type"`
	Name      string      `json:"name"`
	Phone     string      `json:"phone"`
	PhoneCode string      `json:"phone_code"`
	Token     string      `json:"token"`
	Retrieve   string   `json:"retrieve"`
	Seq        string   `json:"seq"`
	Data      interface{} `json:"data"`
}

type last_price_request struct {
	Symbol string `json:"symbol"`
}

type last_price_response struct {
	Retrieve   string `json:"retrieve"`
	Seq        string `json:"seq"`
	TickSeq    uint32 `json:"tick_seq"`
	Symbol     string `json:"symbol"`
	LastPrice  string `json:"last_price"`
	UpdateTime string `json:"update_time"`
}
```
### 56 get last tick 
//const  "**retrieve**":"last_tick"
```
type retrieve_request struct {
	Appid     string      `json:"appid"`
	Sign      string      `json:"sign"`
	SignType  string      `json:"sign_type"`
	Name      string      `json:"name"`
	Phone     string      `json:"phone"`
	PhoneCode string      `json:"phone_code"`
	Token     string      `json:"token"`
	Retrieve   string   `json:"retrieve"`
	Seq        string   `json:"seq"`
	Data      interface{} `json:"data"`
}

type last_tick_request struct {
	Symbol string `json:"symbol"`
}

type last_tick_response struct {
	Retrieve   string   `json:"retrieve"`
	Seq        string   `json:"seq"`
	TickSeq    uint32   `json:"tick_seq"`
	Symbol     string   `json:"symbol"`
	LastPrice  string   `json:"last_price"`
	High       string   `json:"high"`
	Low        string   `json:"low"`
	Open       string   `json:"open"`
	PreClose   string   `json:"close"`
	UpdateTime string   `json:"update_time"`
	Bid        []string `json:"bid"`
	Ask        []string `json:"ask"`
	BidVol     []string `json:"bid_vol"`
	AskVol     []string `json:"ask_vol"`
}
```
### 57 logout
//const  "**retrieve**":"logout"
```
type retrieve_request struct {
	Appid     string      `json:"appid"`
	Sign      string      `json:"sign"`
	SignType  string      `json:"sign_type"`
	Name      string      `json:"name"`
	Phone     string      `json:"phone"`
	PhoneCode string      `json:"phone_code"`
	Token     string      `json:"token"`
	Retrieve   string   `json:"retrieve"`
	Seq        string   `json:"seq"`
	Data      interface{} `json:"data"`
}
type logout_req struct {
}

type logout_resp struct {
	Retrieve string         `json:"retrieve"`
	Seq      string         `json:"seq"`
	Result   reterr.ErrCode `json:"result"`
	Comment  string         `json:"comment"`
}
```
### 58. login by token
  
  POST - https://vk4uikzpgc.execute-api.ap-east-1.amazonaws.com/dev/retrieve

or: wss://3x9r4af6h6.execute-api.ap-east-1.amazonaws.com/dev

//const  "**retrieve**":"login_by_token"
```
// use phone&phone_code to login. NOT Name !!!
type retrieve_request struct {
	Appid     string      `json:"appid"`
	Sign      string      `json:"sign"`
	SignType  string      `json:"sign_type"`
	Name      string      `json:"name"`
	Phone     string      `json:"phone"`
	PhoneCode string      `json:"phone_code"`
	Token     string      `json:"token"`
	Retrieve  string      `json:"retrieve"`
	Data      interface{} `json:"data"`
	Seq       string      `json:"seq"`
}

type login_req struct {
	
}

type login_resp struct {
	NickName string               `json:"nick_name"`
	Logoid   string               `json:"logoid"`
	Assets   []*UserAssets        `json:"assets"`
	Token    string               `json:"token"`
	Retrieve   string   `json:"retrieve"`
	Seq        string   `json:"seq"`
	Result   reterr.ErrCode       `json:"result"`
	Comment  string               `json:"comment"`
}

type UserAssets struct {
	AssetName string `json:"asset_name"`
	Balance   string `json:"balance"`
	Frozen    string `json:"frozen"`
	Uuid      uint64 `json:"uuid"`
	Address   string `json:"address"`
}

```
### 59 kyc random number
  POST - https://vk4uikzpgc.execute-api.ap-east-1.amazonaws.com/dev/retrieve

or: wss://3x9r4af6h6.execute-api.ap-east-1.amazonaws.com/dev

//const  "**retrieve**":"kyc_random_number"
kyc flow: kyc_random_number->upload(files)->submit_kyc->kyc_status->get_upload
```
type retrieve_request struct {
	Appid     string      `json:"appid"`
	Sign      string      `json:"sign"`
	SignType  string      `json:"sign_type"`
	Name      string      `json:"name"`
	Token     string      `json:"token"`
	Retrieve string      `json:"retrieve"`
	Data     interface{} `json:"data"`
	Seq        string   `json:"seq"`
}
type kyc_random_number_req struct {
}

type kyc_random_number_resp struct {
	RandomNumber string `json:"random_number"`
	Retrieve     string `json:"retrieve"`
	Seq          string `json:"seq"`
	Result       int    `json:"result"`
	Comment      string `json:"comment"`
}
```
### 60 cancel withdraw
  POST - https://vk4uikzpgc.execute-api.ap-east-1.amazonaws.com/dev/retrieve

or: wss://3x9r4af6h6.execute-api.ap-east-1.amazonaws.com/dev

//const  "**retrieve**":"cancel_withdraw"
```
type retrieve_request struct {
	Appid     string      `json:"appid"`
	Sign      string      `json:"sign"`
	SignType  string      `json:"sign_type"`
	Name      string      `json:"name"`
	Token     string      `json:"token"`
	Retrieve string      `json:"retrieve"`
	Data     interface{} `json:"data"`
	Seq        string   `json:"seq"`
}

type cancel_withdraw_request struct {
	Id      string `json:"id"`
	PinCode string `json:"pin_code"`
}

type cancel_withdraw_response struct {
	Retrieve string `json:"retrieve"`
	Seq      string `json:"seq"`
	Id       string `json:"id"`
	Result   int    `json:"result"`
	Comment  string `json:"comment"`
}
```
### 61 cancel mbt

//const  "**retrieve**":"cancel_gz_to_dgt"
//const  "**retrieve**":"cancel_dgt_to_gold"
//const  "**retrieve**":"cancel_dgt_to_gz"
```
type retrieve_request struct {
	Appid     string      `json:"appid"`
	Sign      string      `json:"sign"`
	SignType  string      `json:"sign_type"`
	Name      string      `json:"name"`
	Phone     string      `json:"phone"`
	PhoneCode string      `json:"phone_code"`
	Token     string      `json:"token"`
	Retrieve   string   `json:"retrieve"`
	Seq        string   `json:"seq"`
	Data      interface{} `json:"data"`
}

type cancel_mbt_request struct {
	ProposalNo string `json:"proposal_no"`
}

type cancel_mbt_response struct {
	ProposalNo string `json:"proposal_no"`
	Retrieve   string `json:"retrieve"`
	Seq        string `json:"seq"`
	Result     int    `json:"result"`
	Comment    string `json:"comment"`
}
```
### 62 asset notifications for wss or callbcak

//const  "**retrieve**":"transfer_notify"//内部转账
//const  "**retrieve**":"deposit_notify" //大地址链上充值
//const  "**retrieve**":"deposit_payment_notify"//小地址链上充值
//const  "**retrieve**":"withdraw_transfer_payment_notify"//往小地址的链上提币
//const  "**retrieve**":"withdraw_notify"//大地址的链上提币
//const  "**retrieve**":"payment_notify"//扫码充值
//const  "**retrieve**":"frozen_notify"//冻结通知
//const  "**retrieve**":"unfrozen_approve_notify"//解冻成功通知
//const  "**retrieve**":"unfrozen_return_notify"//解冻拒绝通知
```
//const  "**retrieve**":"transfer_notify"
type TransferUpdates struct {
	Retrieve      string `json:"retrieve"`
	Sign          string `json:"sign"`
	Id            string `json:"id,omitempty"`
	AssetName     string `json:"asset_name,omitempty"`
	Amount        string `json:"amount,omitempty"`
	Fee           string `json:"fee,omitempty"`
	UpdateTime    string `json:"update_time,omitempty"`
	OrderId       string `json:"order_id,omitempty"`
	FromPhone     string `json:"from_phone,omitempty"`
	FromPhoneCode string `json:"from_phone_code,omitempty"`
	FromUserNo    string `json:"from_user_no,omitempty"`
	ToPhone       string `json:"to_phone,omitempty"`
	ToPhoneCode   string `json:"to_phone_code,omitempty"`
	ToUserNo      string `json:"to_user_no,omitempty"`
	Status        string `json:"status,omitempty"`
	RefTransferId string `json:"ref_transfer_id,omitempty"`
	CreateTime    string `json:"create_time,omitempty"`
	Merchantid    string `json:"merchantid,omitempty"`
}

//const  "**retrieve**":"deposit_notify"
//appid added@20191220
type DepositUpdates struct {
	Retrieve      string `json:"retrieve"`
	Sign          string `json:"sign"`
	Appid         string `json:"appid"`
	Id            string `json:"id,omitempty"`
	AssetName     string `json:"asset_name,omitempty"`
	Amount        string `json:"amount,omitempty"`
	CreateTime    string `json:"create_time,omitempty"`
	UpdateTime    string `json:"update_time,omitempty"`
	BlockNumber   string `json:"block_number,omitempty"`
	TxHash        string `json:"tx_hash,omitempty"`
	ConfirmNumber uint64 `json:"confirm_number,omitempty"`
	Vid           uint64 `json:"vid,omitempty"`
	FromPhone     string `json:"from_phone,omitempty"`
	FromPhoneCode string `json:"from_phone_code,omitempty"`
	FromUserNo    string `json:"from_user_no,omitempty"`
	ToPhone       string `json:"to_phone,omitempty"`
	ToPhoneCode   string `json:"to_phone_code,omitempty"`
	ToUserNo      string `json:"to_user_no,omitempty"`
	Status        string `json:"status,omitempty"`
}

//const  "**retrieve**":"withdraw_notify"
//appid added@20191220
type WithdrawUpdates struct {
	Retrieve      string `json:"retrieve"`
	Sign          string `json:"sign"`
	Appid         string `json:"appid"`
	Id            string `json:"id,omitempty"`
	AssetName     string `json:"asset_name,omitempty"`
	Amount        string `json:"amount,omitempty"`
	Fee           string `json:"fee,omitempty"`
	CreateTime    string `json:"create_time,omitempty"`
	UpdateTime    string `json:"update_time,omitempty"`
	BlockNumber   string `json:"block_number,omitempty"`
	TxHash        string `json:"tx_hash,omitempty"`
	FromUser      string `json:"from_user,omitempty"`
	ConfirmNumber uint64 `json:"confirm_number,omitempty"`
	Vid           uint64 `json:"vid,omitempty"`
	FromPhone     string `json:"from_phone,omitempty"`
	FromPhoneCode string `json:"from_phone_code,omitempty"`
	FromUserNo    string `json:"from_user_no,omitempty"`
	ToPhone       string `json:"to_phone,omitempty"`
	ToPhoneCode   string `json:"to_phone_code,omitempty"`
	ToUserNo      string `json:"to_user_no,omitempty"`
	Status        string `json:"status,omitempty"`
	Merchantid    string `json:"merchantid,omitempty"`
	OrderId       string `json:"order_id,omitempty"`
}

//const  "**retrieve**":"payment_notify"
type PaymentUpdates struct {
	Retrieve      string `json:"retrieve"`
	Sign          string `json:"sign"`
	Id            string `json:"id,omitempty"`
	AssetName     string `json:"asset_name,omitempty"`
	Amount        string `json:"amount,omitempty"`
	Fee           string `json:"fee,omitempty"`
	UpdateTime    string `json:"update_time,omitempty"`
	OrderId       string `json:"order_id,omitempty"`
	FromPhone     string `json:"from_phone,omitempty"`
	FromPhoneCode string `json:"from_phone_code,omitempty"`
	FromUserNo    string `json:"from_user_no,omitempty"`
	ToPhone       string `json:"to_phone,omitempty"`
	ToPhoneCode   string `json:"to_phone_code,omitempty"`
	ToUserNo      string `json:"to_user_no,omitempty"`
	Merchantid    string `json:"merchantid,omitempty"`
	MerchantName  string `json:"merchant_name,omitempty"`
	Status        string `json:"status,omitempty"`
	CreateTime    string `json:"create_time,omitempty"`
}

//const  "**retrieve**":"frozen_notify"
// success only
//const  "**retrieve**":"unfrozen_notify"
// approve or reject 
type FrozenUpdates struct {
	Retrieve      string `json:"retrieve"`
	Sign          string `json:"sign"`
	Id            string `json:"id,omitempty"`
	AssetName     string `json:"asset_name,omitempty"`
	Amount        string `json:"amount,omitempty"`
	UpdateTime    string `json:"update_time,omitempty"`
	OrderId       string `json:"order_id,omitempty"`
	FromPhone     string `json:"from_phone,omitempty"`
	FromPhoneCode string `json:"from_phone_code,omitempty"`
	FromUserNo    string `json:"from_user_no,omitempty"`
	ToPhone       string `json:"to_phone,omitempty"`
	ToPhoneCode   string `json:"to_phone_code,omitempty"`
	ToUserNo      string `json:"to_user_no,omitempty"`
	Merchantid    string `json:"merchantid,omitempty"`
	Status        string `json:"status,omitempty"`
	CreateTime    string `json:"create_time,omitempty"`
}

//const  "**retrieve**":"redeem_notify"
//the amount released would trigger unfrozen_notify
type RedeemUpdates struct {
	Retrieve   string `json:"retrieve"`
	Sign       string `json:"sign"`
	Id         string `json:"id"`
	FrozenId   string `json:"frozen_id"`
	OrderId    string `json:"order_id"`
	Status     string `json:"status"` //STATUS_UNFROZEN_APPROVED,STATUS_UNFROZEN_REJECTED
	UpdateTime string `json:"update_time"`
}

//const  "**retrieve**":"deposit_payment_notify"
type DepositPaymentUpdates struct {
		Retrieve        string `json:"retrieve"`
		Sign            string `json:"sign"`
		Id              string `json:"id,omitempty"`
		AssetName       string `json:"asset_name,omitempty"`
		Amount          string `json:"amount,omitempty"`
		Fee             string `json:"fee,omitempty"`
		UpdateTime      string `json:"update_time,omitempty"`
		OrderId         string `json:"order_id,omitempty"`
		FromPhone       string `json:"from_phone,omitempty"`
		FromPhoneCode   string `json:"from_phone_code,omitempty"`
		FromUserNo      string `json:"from_user_no,omitempty"`
		DepositFromAddr string `json:"deposit_from_address"`
		DepositToAddr   string `json:"deposit_to_address"`
		ToPhone         string `json:"to_phone,omitempty"`
		ToPhoneCode     string `json:"to_phone_code,omitempty"`
		ToUserNo        string `json:"to_user_no,omitempty"`
		Merchantid      string `json:"merchantid,omitempty"`
		MerchantName    string `json:"merchant_name,omitempty"`
		Status          string `json:"status,omitempty"`
		CreateTime      string `json:"create_time,omitempty"`
	}
//const  "**retrieve**":"withdraw_transfer_payment_notify"
	type WithdrawTransferPaymentUpdates struct {
		Retrieve               string `json:"retrieve"`
		Sign                   string `json:"sign"`
		Id                     string `json:"id,omitempty"`
		AssetName              string `json:"asset_name,omitempty"`
		Amount                 string `json:"amount,omitempty"`
		Fee                    string `json:"fee,omitempty"`
		UpdateTime             string `json:"update_time,omitempty"`
		OrderId                string `json:"order_id,omitempty"`
		FromPhone              string `json:"from_phone,omitempty"`
		FromPhoneCode          string `json:"from_phone_code,omitempty"`
		FromUserNo             string `json:"from_user_no,omitempty"`
		ToPhone                string `json:"to_phone,omitempty"`
		ToPhoneCode            string `json:"to_phone_code,omitempty"`
		ToUserNo               string `json:"to_user_no,omitempty"`
		Merchantid             string `json:"merchantid,omitempty"`
		MerchantName           string `json:"merchant_name,omitempty"`
		Status                 string `json:"status,omitempty"`
		CreateTime             string `json:"create_time,omitempty"`
		WithdrawFromUserNo     string `json:"withdraw_from_user_no,omitempty"`
		WithdrawFromMerchantid string `json:"withdraw_from_merchantid,omitempty"`
		DepositToAddr          string `json:"deposit_to_address"`
	}
//callback should return back this response with success result:0
type Response struct {
	Retrieve string `json:"retrieve"`
	Seq      string `json:"seq"`
	Result   int    `json:"result"`
	Comment  string `json:"comment"`
}
```
### 63 is register
//const  "**retrieve**":"isregister"
```
type retrieve_request struct {
	Appid     string      `json:"appid"`
	Sign      string      `json:"sign"`
	SignType  string      `json:"sign_type"`
	Name      string      `json:"name"`
	Phone     string      `json:"phone"`
	PhoneCode string      `json:"phone_code"`
	Token     string      `json:"token"`
	Retrieve   string   `json:"retrieve"`
	Seq        string   `json:"seq"`
	Data      interface{} `json:"data"`
}
type is_register_req struct {
	Name      string `json:"name"`
	Phone     string `json:"phone"`
	PhoneCode string `json:"phone_code"`
	Email     string `json:"email"`
}

type is_register_resp struct {
	IsRegister string         `json:"is_registered"`
	Retrieve   string         `json:"retrieve"`
	Seq        string         `json:"seq"`
	Result     reterr.ErrCode `json:"result"`
	Comment    string         `json:"comment"`
}
```
### 64 change_password
//const  "**retrieve**":"change_password"
```
type retrieve_request struct {
	Appid     string      `json:"appid"`
	Sign      string      `json:"sign"`
	SignType  string      `json:"sign_type"`
	Name      string      `json:"name"`
	Phone     string      `json:"phone"`
	PhoneCode string      `json:"phone_code"`
	Token     string      `json:"token"`
	Retrieve   string   `json:"retrieve"`
	Seq        string   `json:"seq"`
	Data      interface{} `json:"data"`
}

type change_psw_req struct {
	NewPassword string `json:"new_password"`
	SmsCode     string `json:"sms_code"`
	GoogleCode  string `json:"google_code"`
}

type change_psw_resp struct {
	Retrieve string         `json:"retrieve"`
	Seq      string         `json:"seq"`
	Result   reterr.ErrCode `json:"result"`
	Comment  string         `json:"comment"`
}

```
### 65 tx list
//const  "**retrieve**":"tx_list"

**all in one list**
TYPE_DEPOSIT: status empty 
TYPE_TRANSFER(TYPE_SEND,TYPE_RECV):STATUS_PENDING,STATUS_FINISHED
TYPE_WITHDRAW: STATUS_INITIAL,STATUS_PROCESSING,STATUS_SIGNED,STATUS_FINISHED,STATUS_CANCELED,STATUS_PENDING,STATUS_PENDING_WALLET,STATUS_REJECTED
TYPE_PAYMENT:STATUS_INITIAL,STATUS_SUBMITED,STATUS_PAID,STATUS_REJECTED
TYPE_REDEEM:STATUS_INITIAL,STATUS_SUBMITED,STATUS_FROZEN,STATUS_UNFROZEN_APPROVED,STATUS_UNFROZEN_REJECTED
TYPE_UNFROZEN:STATUS_UNFROZEN_APPROVED,STATUS_UNFROZEN_REJECTED

```
type tx_list_request struct {
	UserNo       string `json:"user_no"`
	User         string `json:"user"`
	Type         string `json:"type"`
	AcceptedFrom string `json:"accepted_from"` //APP, API, ADMIN, SUPER, SYSTEM
	Asset        string `json:"asset"`
	StartTime    int64  `json:"start_time"`
	EndTime      int64  `json:"end_time"`
	PageNumber   int64  `json:"page_number"`
	PageSize     int64  `json:"page_size"`
}
type tx_in_one struct {
	Id            string `json:"id"`
	Asset         string `json:"asset"`
	Amount        string `json:"amount"`
	Fee           string `json:"fee"`
	FeePaidBy     string `json:"fee_paid_by"`
	PaidTotal     string `json:"paid_total"`
	OrderId       string `json:"order_id"`
	Status        string `json:"status"`
	Type          string `json:"type"` // TYPE_SEND,TYPE_RECV,TYPE_WITHDRAW,TYPE_DEPOSIT,TYPE_REDEEM,TYPE_PAYMENT,TYPE_RECV_PAYMENT,TYPE_FROZEN,TYPE_UNFROZEN,TYPE_RECV_UNFROZEN, TYPE_SEND_RETURN,TYPE_RECV_RETURN,TYPE_PAYMENT_RETURN,TYPE_RECV_PAYMENT_RETURN
	FromPhone     string `json:"from_phone"`
	FromPhoneCode string `json:"from_phone_code"`
	FromUserNo    string `json:"from_user_no"`
	FromUser      string `json:"from_user"`
	FromAddr      string `json:"from_addr,omitempty"`
	FromName      string `json:"from_name"`
	ToPhone       string `json:"to_phone,omitempty"` //for payment privacy, not showing merchant's phone
	ToPhoneCode   string `json:"to_phone_code,omitempty"`
	ToUserNo      string `json:"to_user_no"`
	ToUser        string `json:"to_user"`
	ToAddr        string `json:"to_addr,omitempty"`
	ToName        string `json:"to_name"`
	CreateTime    string `json:"create_time"`
	Merchantid    string `json:"merchantid,omitempty"`
	FromBalance   string `json:"from_balance"`
	FromFrozen    string `json:"from_frozen"`
	ToBalance     string `json:"to_balance"`
	ToFrozen      string `json:"to_frozen"`
	AcceptedFrom  string `json:"accepted_from"`
	GasFee        string `json:"gas_fee",omitempty`
	OriginId      string `json:"origin_id"`
	UpdateTime    string `json:"update_time"`
	ReturnRefid   string `json:"return_refid"`
	PaymentType   string `json:"payment_type"` //empty or TYPE_SUBASSET
}
type tx_list_response struct {
	TxList       []*tx_in_one `json:"tx_list"`
	UserNo       string       `json:"user_no"`
	User         string       `json:"user"`
	Type         string       `json:"type"`
	AcceptedFrom string       `json:"accepted_from"`
	Asset        string       `json:"asset"`
	StartTime    int64        `json:"start_time"`
	EndTime      int64        `json:"end_time"`
	PageNumber   int64        `json:"page_number"`
	PageSize     int64        `json:"page_size"`
	Total        int64        `json:"total"`
	Retrieve     string       `json:"retrieve"`
	Seq          string       `json:"seq"`
	Result       int          `json:"result"`
	Comment      string       `json:"comment"`
}
```

### 66 calc fee
//const  "**retrieve**":"calc_fee"
```
type retrieve_request struct {
	Appid     string      `json:"appid"`
	Sign      string      `json:"sign"`
	SignType  string      `json:"sign_type"`
	Name      string      `json:"name"`
	Phone     string      `json:"phone"`
	PhoneCode string      `json:"phone_code"`
	Token     string      `json:"token"`
	Retrieve   string   `json:"retrieve"`
	Seq        string   `json:"seq"`
	Data      interface{} `json:"data"`
}

type calc_fee_request struct {
	AssetName string `json:"asset_name"`
	Amount    string `json:"amount"`
	Type      string `json:"type"`    // TYPE_WITHDRAW,TYPE_TRANSFER,TYPE_REDEEM
	PaidBy    string `json:"paid_by"` // "FROM","TO", empty default "FROM"
}

type calc_fee_response struct {
	Fee       string `json:"fee"` // denomiated by AssetName
	AssetName string `json:"asset_name"`
	Amount    string `json:"amount"`
	Type      string `json:"type"`    // TYPE_WITHDRAW,TYPE_TRANSFER,TYPE_REDEEM
	PaidBy    string `json:"paid_by"` // "FROM","TO", empty default "FROM"
	Retrieve  string `json:"retrieve"`
	Seq       string `json:"seq"`
	Result    int    `json:"result"`
	Comment   string `json:"comment"`
}
```
### 67 submit payment
//const  "**retrieve**":"submit_payment"
//const "**retrieve**":"submit_payment_by_userno"
//const  "**retrieve**":"submit_payment_no_address"
```
type submit_payment_request struct {
	AssetName     string `json:"asset_name"`
	Amount        string `json:"amount"`
	FromPhone     string `json:"from_phone"`
	FromPhoneCode string `json:"from_phone_code"`
	FeePaidBy     string `json:"fee_paid_by"`   // "FROM","TO", empty default "FROM"
	OrderId       string `json:"order_id"`      // order id from merchant
	ToPhone       string `json:"to_phone"`      // reciever
	ToPhoneCode   string `json:"to_phone_code"` // reciever
	Merchantid    string `json:"merchantid"`
	MerchantName  string `json:"merchant_name"`
	CallbackUrl   string `json:"callback_url"` // after pay fi, notify  to url for merchant
	RedirectUrl   string `json:"redirect_url"` // after pay fi, redirect to url for user
	PinCode       string `json:"pin_code"`
	SmsCode       string `json:"sms_code"`
	GoogleCode    string `json:"google_code"`
}

type submit_payment_response struct {
	Id  string `json:"id"`  // system order id
	Url string `json:"url"` // system payment url , used by merchant, redirect to user

	AssetName     string `json:"asset_name"`
	Amount        string `json:"amount"`
	FromPhone     string `json:"from_phone"`
	FromPhoneCode string `json:"from_phone_code"`

	Fee       string `json:"fee"`         // denominated by AssetName
	FeePaidBy string `json:"fee_paid_by"` // "FROM","TO", empty default "FROM"

	OrderId      string `json:"order_id"`      // order id from merchant
	ToPhone      string `json:"to_phone"`      // reciever
	ToPhoneCode  string `json:"to_phone_code"` // reciever
	Merchantid   string `json:"merchantid"`
	MerchantName string `json:"merchant_name"`
	Retrieve     string `json:"retrieve"`
	Seq          string `json:"seq"`
	Result       int    `json:"result"`
	Comment      string `json:"comment"`
}
```
### 68 pay
//const  "**retrieve**":"pay"
//const  "**retrieve**":"pay_no_address"
```
type pay_request struct {
	OrderId string `json:"order_id"`
	PinCode string `json:"pin_code"`
}
type pay_response struct {
	OrderId  string `json:"order_id"`
	Retrieve string `json:"retrieve"`
	Seq      string `json:"seq"`
	Result   int    `json:"result"`
	Comment  string `json:"comment"`
}

```
### 69 submit_frozen
//const  "**retrieve**":"submit_frozen"
```
type submit_frozen_request struct {
	AssetName     string `json:"asset_name"`
	Amount        string `json:"amount"`
	FromPhone     string `json:"from_phone"`
	FromPhoneCode string `json:"from_phone_code"`
	OrderId       string `json:"order_id"`      // order id from merchant
	ToPhone       string `json:"to_phone"`      // reciever,optional
	ToPhoneCode   string `json:"to_phone_code"` // reciever,optional
}

type submit_frozen_response struct {
	Id  string `json:"id"`  // system order id
	Url string `json:"url"` // system payment url , used by merchant, redirect to user

	AssetName     string `json:"asset_name"`
	Amount        string `json:"amount"`
	FromPhone     string `json:"from_phone"`
	FromPhoneCode string `json:"from_phone_code"`

	OrderId     string `json:"order_id"`      // order id from merchant
	ToPhone     string `json:"to_phone"`      // reciever
	ToPhoneCode string `json:"to_phone_code"` // reciever
	Retrieve    string `json:"retrieve"`
	Seq         string `json:"seq"`
	Result      int    `json:"result"`
	Comment     string `json:"comment"`
}
```
### 70 frozen-deleted-no-this-method-now
//const  "**retrieve**":"frozen"
```
type frozen_request struct {
	OrderId string `json:"order_id"`
	PinCode string `json:"pin_code"`
}
type frozen_response struct {
	OrderId  string `json:"order_id"`
	Retrieve string `json:"retrieve"`
	Seq      string `json:"seq"`
	Result   int    `json:"result"`
	Comment  string `json:"comment"`
}
```
### 71 approve_frozen
//const  "**retrieve**":"approve_frozen"
//const  "**retrieve**":"approve_frozen_no_address"
```
type approve_frozen_request struct {
	OrderId      string `json:"order_id"`       //maker orderid
	Type         string `json:"type"`           // "TYPE_UNFROZEN_APPROVED", "TYPE_UNFROZEN_REJECTED"
	TakerOrderId string `json:"taker_order_id"` // order id from merchant
	ToPhone      string `json:"to_phone"`       // reciever
	ToPhoneCode  string `json:"to_phone_code"`  // reciever
	Amount       string `json:"amount"`         // can be partial or all amount
}
type approve_frozen_response struct {
	OrderId      string `json:"order_id"`       //maker orderid
	Type         string `json:"type"`
	TakerOrderId string `json:"taker_order_id"` // taker order id from merchant
	ToPhone      string `json:"to_phone"`       // reciever
	ToPhoneCode  string `json:"to_phone_code"`  // reciever
	Amount       string `json:"amount"`
	Id           string `json:"id"`             // unfrozen id
	Retrieve     string `json:"retrieve"`
	Seq          string `json:"seq"`
	Result       int    `json:"result"`
	Comment      string `json:"comment"`
}
```
### 72 submit_redeem 
//const  "**retrieve**":"submit_redeem"
```
type submit_redeem_request struct {
	GzAmount        string `json:"gz_amount"`
	GoldAmount      string `json:"gold_amount"`
	GzAdminFee      string `json:"gz_admin_fee"`
	GzShippingFee   string `json:"gz_shipping_fee"`
	GzPaidTotal     string `json:"gz_paid_total"`
	DetailAddress   string `json:"detail_address"`
	DeliveryAddress string `json:"delivery_address"`
	TermsCondition  string `json:"terms_condition"`
	OrderId         string `json:"order_id"`     // order id from merchant
	CallbackUrl     string `json:"callback_url"` // after pay fi, notify  to url for merchant
	RedirectUrl     string `json:"redirect_url"` // after pay fi, redirect to url for user
}

type submit_redeem_response struct {
	Id       string `json:"id"`        // system order id
	FrozenId string `json:"frozen_id"` // system frozen id
	Url      string `json:"url"`       // system redeem confirm url , used by merchant, redirect to user

	GzAmount        string `json:"gz_amount"`
	GoldAmount      string `json:"gold_amount"`
	GzAdminFee      string `json:"gz_admin_fee"`
	GzShippingFee   string `json:"gz_shipping_fee"`
	GzPaidTotal     string `json:"gz_paid_total"`
	DetailAddress   string `json:"detail_address"`
	DeliveryAddress string `json:"delivery_address"`
	TermsCondition  string `json:"terms_condition"`
	OrderId         string `json:"order_id"`

	Retrieve string `json:"retrieve"`
	Seq      string `json:"seq"`
	Result   int    `json:"result"`
	Comment  string `json:"comment"`
}

```
### 73 submit_digold_kyc
//const  "**retrieve**":"submit_digold_kyc" 
```
type submit_digold_kyc_request struct {
	RandomNumber             string `json:"random_number"`
	FullName                 string `json:"full_name"`
	Nationality              string `json:"nationality"`
	IdNumber                 string `json:"id_number"`
	IdType                   string `json:"id_type"` // "IDCard","Passport"
	ContactAddress           string `json:"contact_address"`
	Telephone                string `json:"telephone"`
	Email                    string `json:"email"`
	Occupation               string `json:"occupation"`
	AnnualIncome             string `json:"annual_income"`
	SourceOfFund             string `json:"source_of_fund"`
	SourceOfFundOption       string `json:"source_of_fund_option"`
	ReasonOpenAccount        string `json:"reason_open_account"`
	HaveOtherWallet          string `json:"have_other_wallet"`
	HaveOtherWalletUSDAmount string `json:"have_other_wallet_usd_amount"`
	IdCardFront              string `json:"id_card_front"`
	IdCardBack               string `json:"id_card_back"`
	ProofOfAddress           string `json:"proof_of_address"`
	Selfie                   string `json:"selfie"`
	TermsConditions          string `json:"terms_conditions"`
}

type submit_digold_kyc_response struct {
	Retrieve string `json:"retrieve"`
	Seq      string `json:"seq"`
	Result   int    `json:"result"`
	Comment  string `json:"comment"`
}
```
### 74 digold_kyc_status
//const  "**retrieve**":"digold_kyc_status" 
```
type kyc_status_request struct {
	Detail string `json:"detail"` // empty for status only
}
type digoldKyc struct {
	Id                       string `json:"id"`
	Appid                    string `json:"appid"`
	UserNo                   string `json:"user_no"`
	User                     string `json:"user"`
	RandomNumber             string `json:"random_number"`
	FullName                 string `json:"full_name"`
	Nationality              string `json:"nationality"`
	IdNumber                 string `json:"id_number"`
	IdType                   string `json:"id_type"`
	ContactAddress           string `json:"contact_address"`
	Telephone                string `json:"telephone"`
	Email                    string `json:"email"`
	Occupation               string `json:"occupation"`
	AnnualIncome             string `json:"annual_income"`
	SourceOfFund             string `json:"source_of_fund"`
	SourceOfFundOption       string `json:"source_of_fund_option"`
	ReasonOpenAccount        string `json:"reason_open_account"`
	HaveOtherWallet          string `json:"have_other_wallet"`
	HaveOtherWalletUSDAmount string `json:"have_other_wallet_usd_amount"`
	IdCardFront              string `json:"id_card_front"`
	IdCardBack               string `json:"id_card_back"`
	ProofOfAddress           string `json:"proof_of_address"`
	Selfie                   string `json:"selfie"`
	TermsConditions          string `json:"terms_conditions"`
	CreateTime               string `json:"create_time"`
	UpdateTime               string `json:"update_time"`
	Status                   string `json:"status"`
	Comment                  string `json:"comment"`
	InternalComment          string `json:"internal_comment"`
}
type digold_kyc_status_response struct {
	Kyc      *digoldKyc `json:"kyc",omitempty`
	/*
	Initial  = 0;
	Pending  = 1;
	Inactive = 2;
	Active   = 3;
	Reject   = 4;
	NameFilled = 5;
	*/
	Status   string     `json:"status"`
	Retrieve string     `json:"retrieve"`
	Seq      string     `json:"seq"`
	Result   int        `json:"result"`
	Comment  string     `json:"comment"`
}
```
### 75 submit_mint
//const  "**retrieve**":"submit_mint" 
```

type submit_mint_request struct {
	OrderId   string `json:"order_id"`
	AssetName string `json:"asset_name"`
	Amount    string `json:"amount"`
}

type submit_mint_response struct {
	Id          string `json:"id"`
	OrderId     string `json:"order_id"`
	AssetName   string `json:"asset_name"`
	Amount      string `json:"amount"`
	RedirectUrl string `json:"redirect_url"` //
	Retrieve    string `json:"retrieve"`
	Seq         string `json:"seq"`
	Result      int    `json:"result"`
	Comment     string `json:"comment"`
}
```
### 76 submit_burn
//const  "**retrieve**":"submit_burn" 
```

type submit_burn_request struct {
	OrderId   string `json:"order_id"`
	AssetName string `json:"asset_name"`
	Amount    string `json:"amount"`
}

type submit_burn_response struct {
	Id          string `json:"id"`
	OrderId     string `json:"order_id"`
	AssetName   string `json:"asset_name"`
	Amount      string `json:"amount"`
	RedirectUrl string `json:"redirect_url"` //
	Retrieve    string `json:"retrieve"`
	Seq         string `json:"seq"`
	Result      int    `json:"result"`
	Comment     string `json:"comment"`
}
```
## app user config's xapp feature and wi/wo asset address
refer to READMEXAPP.md
## sign by client sign_type should be SHA256WithRSAClient to differ Buser's sign

### 77 update_user_device
//const  "**retrieve**":"update_user_device" 
```
type retrieve_request struct {
	Appid     string      `json:"appid"`
	Sign      string      `json:"sign"`
	SignType  string      `json:"sign_type"`
	Phone     string      `json:"phone"`
	PhoneCode string      `json:"phone_code"`
	Retrieve   string     `json:"retrieve"`
	Seq        string     `json:"seq"`
	Data      interface{} `json:"data"`
}
type update_user_device_req struct {
	DeviceId  string `json:"device_id"`
	PublicKey string `json:"public_key"`
	SmsCode   string `json:"sms_code"`
	Pushid    string `json:"pushid"`
}

type update_user_device_resp struct {
	Retrieve string         `json:"retrieve"`
	Seq      string         `json:"seq"`
	Result   reterr.ErrCode `json:"result"`
	Comment  string         `json:"comment"`
}
```
### 77 kyc_terms
//const  "**retrieve**":"kyc_terms" 
```
type kyc_terms_request struct {
}
type kyc_terms_response struct {
	Body     string         `json:"body"` // base64 encoded
	Retrieve string         `json:"retrieve"`
	Seq      string         `json:"seq"`
	Result   reterr.ErrCode `json:"result"`
	Comment  string         `json:"comment"`
}
```
### 78 update user password
//const  "**retrieve**":"update_password" 
```
type update_password_req struct {
	OldPassword string `json:"old_password"`
	NewPassword string `json:"new_password"`
}

type update_password_resp struct {
	Retrieve string         `json:"retrieve"`
	Seq      string         `json:"seq"`
	Result   reterr.ErrCode `json:"result"`
	Comment  string         `json:"comment"`
}
```
### 79
//const  "**retrieve**":"last_tx"
```

type last_tx_request struct {
}
type last_tx_response struct {
	Id        string `json:"id"`
	AssetName string `json:"asset_name"`
	Amount    string `json:"amount"`
	Type      string `json:"type"`
	/*
		TYPE_SEND = 0;
		TYPE_RECV = 1;
		TYPE_PAYMENT       = 2;
		TYPE_RECV_PAYMENT  = 3;
		TYPE_WITHDRAW = 4;
		TYPE_DEPOSIT  = 5;
		TYPE_FROZEN   = 6;
		TYPE_UNFROZEN = 7;
		TYPE_RECV_UNFROZEN = 8;
		TYPE_REDEEM   = 9;
	*/
	Time     string `json:"time"`
	Retrieve string `json:"retrieve"`
	Seq      string `json:"seq"`
	Result   int    `json:"result"`
	Comment  string `json:"comment"`
}
```
### 80
//const  "**retrieve**":"update_enable"
```
//ENABLED, DISABLED
type update_enable_req struct {
	BioEnable string `json:"bio_enable"`
	SmsEnable string `json:"sms_enable"`
	SmsCode   string `json:"sms_code"`
	GoogleCode  string `json:"google_code"`
}
type update_enable_resp struct {
	BioEnable string `json:"bio_enable"`
	SmsEnable string `json:"sms_enable"`
	Retrieve  string `json:"retrieve"`
	Seq       string `json:"seq"`
	Result    int    `json:"result"`
	Comment   string `json:"comment"`
}
```
### 81 bind_merchant_user
//const  "**retrieve**":"bind_merchant_user"
```
type bind_merchant_user_req struct {
	RefId        string `json:"ref_id"`
	MerchantId   string `json:"merchant_id"`
	MerchantName string `json:"merchant_name"`
}
type bind_merchant_user_resp struct {
	RefId        string `json:"ref_id"`
	MerchantId   string `json:"merchant_id"`
	MerchantName string `json:"merchant_name"`
	Retrieve     string `json:"retrieve"`
	Seq          string `json:"seq"`
	Result       int    `json:"result"`
	Comment      string `json:"comment"`
}
//the struct below used to notify callback merchant
type bind_notify struct {
	Retrieve string `json:"retrieve"`
	Sign     string `json:"sign"`
	UserNo   string `json:"user_no"`

	RefId        string `json:"ref_id"`
	MerchantId   string `json:"merchant_id"`
	MerchantName string `json:"merchant_name,omitempty"`
	CreateTime   string `json:"create_time"`
}
```
### 82 delete friend
//const  "**retrieve**":"delete_friend"
```
type delete_friend_req struct {
	UserNo    string `json:"user_no"`
	Phone     string `json:"phone"`
	PhoneCode string `json:"phone_code"`
}

type delete_friend_resp struct {
	UserNo    string `json:"user_no"`
	Phone     string `json:"phone"`
	PhoneCode string `json:"phone_code"`
	Retrieve  string `json:"retrieve"`
	Seq       string `json:"seq"`
	Result    int    `json:"result"`
	Comment   string `json:"comment"`
}
```
### 83 batch_get_logo
//const  "**retrieve**":"batch_get_logo"
//https only
```
type batch_get_logo_request struct {
	Fileids []string `json:"fileids"`
}
type batch_get_logo_response struct {
	Fileids  []string `json:"fileids"`
	Bodys    []string `json:"bodys"`
	Retrieve string   `json:"retrieve"`
	Seq      string   `json:"seq"`
}
```
### 84 resp extension
```
errcode = NEED_RESET_PASSWORD: need_reset_password
errcode = TOKEN_KICK_OUT: device_id&time_stamp
errcode = PINCODE_TOO_FREQUENT&PINCODE_INVALID: pin_code_err_count
type RespExt struct {
	NeedResetPassword bool           `json:"need_reset_password,omitempty"`
	DeviceId          string         `json:"device_id,omitempty"`
	TimeStamp         int64          `json:"time_stamp,omitempty"`
	PinCodeErrCount   int64          `json:"pin_code_err_count,omitempty"`
	Retrieve          string         `json:"retrieve"`
	Seq               string         `json:"seq"`
	Result            reterr.ErrCode `json:"result"`
	Comment           string         `json:"comment"`
}
```
### 85 heart_beat
//const  "**retrieve**":"heart_beat"
```
type retrieve_request struct {
	Appid     string      `json:"appid"`
	Sign      string      `json:"sign"`
	SignType  string      `json:"sign_type"`
	Phone     string      `json:"phone"`
	PhoneCode string      `json:"phone_code"`
	Retrieve   string     `json:"retrieve"`
	Seq        string     `json:"seq"`
	Data      interface{} `json:"data"`
}
```
### 86 enable two fa of google code
//const  "**retrieve**":"enable_twofa"
```
type enable_twofa_req struct {
	SmsCode string `json:"sms_code"`
}
type enable_twofa_resp struct {
	QrCode   string `json:"qr_code"`
	Secret   string `json:"secret"`
	Retrieve string `json:"retrieve"`
	Seq      string `json:"seq"`
	Result   int    `json:"result"`
	Comment  string `json:"comment"`
}
```
### 87 user_status
//const  "**retrieve**":"user_status"
```
type user_status_resp struct {
	KycStatus   string `json:"kyc_status"`
	BioEnable   string `json:"bio_enable"`
	SmsEnable   string `json:"sms_enable"`
	TwofaEnable string `json:"twofa_enable"`
	Retrieve    string `json:"retrieve"`
	Seq         string `json:"seq"`
	Result      int    `json:"result"`
	Comment     string `json:"comment"`
}
```

### 88 踢出通知retrieve：kickout

### 89 get_google_code
//const  "**retrieve**":"get_google_code"
```
type get_google_code_req struct {
	SmsCode string `json:"sms_code"` //required when bind again
}
type get_google_code_resp struct {
	QrCode   string `json:"qr_code"`
	Secret   string `json:"secret"`
	Retrieve string `json:"retrieve"`
	Seq      string `json:"seq"`
	Result   int    `json:"result"`
	Comment  string `json:"comment"`
}
```
### 90 bind_google_code
//const  "**retrieve**":"bind_google_code"
```
type bind_google_code_req struct {
	SmsCode    string `json:"sms_code"`
	Secret     string `json:"secret"` //if secret is empty, will clear the binding
	GoogleCode string `json:"google_code"` //add this code to verify
}
type bind_google_code_resp struct {
	Retrieve string `json:"retrieve"`
	Seq      string `json:"seq"`
	Result   int    `json:"result"`
	Comment  string `json:"comment"`
}
```
### 91 address_query
//const  "**retrieve**":"address_query"
```
type address_query_req struct {
	Address string `json:"address"`
}
type address_query_resp struct {
	Address      string         `json:"address"`
	Phone        string         `json:"phone"`
	PhoneCode    string         `json:"phone_code"`
	UserNo       string         `json:"user_no"`
	NickName     string         `json:"nick_name"`
	Status       string         `json:"status"`      //STATUS_NOT_FOUND,STATUS_OCCUPIED
	MerchantId   string         `json:"merchant_id"` //if merchant id is not empty, it is subasset
	MerchantName string         `json:"merchant_name"`
	Logoid       string         `json:"logoid"`
	Type         string         `json:"type"` //TYPE_WALLET_ASSET,TYPE_MERCHANT_SUBASSET
	Retrieve     string         `json:"retrieve"`
	Seq          string         `json:"seq"`
	Result       reterr.ErrCode `json:"result"`
	Comment      string         `json:"comment"`
}
```
### 92 enable_google_code
//const  "**retrieve**":"enable_google_code"
```
type enable_google_code_req struct {
	SmsCode    string `json:"sms_code"`
	GoogleCode string `json:"google_code"`
	Enable     string `json:"enable"` //DISABLED,ENABLED
}
type enable_google_code_resp struct {
	Retrieve string `json:"retrieve"`
	Seq      string `json:"seq"`
	Result   int    `json:"result"`
	Comment  string `json:"comment"`
}
```
### 93 check_sms
//const  "**retrieve**":"check_sms"
//one minute check twice as the limit
```
type check_sms_request struct {
	Usage     int    `json:"usage"` // 0:register 1:change password 2:change telephone 3:transfer 4:withdraw 5:frozen
	PhoneCode string `json:"phone_code"`
	Phone     string `json:"phone"`
	SmsCode   string `json:"sms_code"`
}
type check_sms_response struct {
	Retrieve string         `json:"retrieve"`
	Seq      string         `json:"seq"`
	Result   reterr.ErrCode `json:"result"`
	Comment  string         `json:"comment"`
}
```
### 94 is_google_code_enable
//const  "**retrieve**":"is_google_code_enable"
```
type is_google_code_enable_req struct {
	UserNo    string `json:"user_no"`
	Phone     string `json:"phone"`
	PhoneCode string `json:"phone_code"`
	Email     string `json:"email"`
}

type is_google_code_enable_resp struct {
	Status   string         `json:"status"` //BINDED,NOT_BINDED,DISABLED,ENABLED
	Retrieve string         `json:"retrieve"`
	Seq      string         `json:"seq"`
	Result   reterr.ErrCode `json:"result"`
	Comment  string         `json:"comment"`
}
```
### 95 email_list
//const  "**retrieve**":"email_list"
```
type email_list_req struct {
}
type email_list_resp struct {
	List     []string       `json:"lsit"`
	Retrieve string         `json:"retrieve"`
	Seq      string         `json:"seq"`
	Result   reterr.ErrCode `json:"result"`
	Comment  string         `json:"comment"`
}
```
### 96 send_email
//const  "**retrieve**":"send_email"
```
type send_email_request struct {
	Usage int    `json:"usage"` // 0:register 1:change password 2:change telephone 3:transfer 4:withdraw 5:frozen
	Email string `json:"email"`
}

type send_email_response struct {
	Retrieve string `json:"retrieve"`
	Seq      string `json:"seq"`
	Result   int    `json:"result"`
	Comment  string `json:"comment"`
}
```
### 97 check_email_code
//const  "**retrieve**":"check_email_code"
```
type check_email_code_request struct {
	Usage     int    `json:"usage"` // 0:register 1:change password 2:change telephone 3:transfer 4:withdraw 5:frozen
	Email     string `json:"email"`
	EmailCode string `json:"email_code"`
}
type check_email_code_response struct {
	Retrieve string         `json:"retrieve"`
	Seq      string         `json:"seq"`
	Result   reterr.ErrCode `json:"result"`
	Comment  string         `json:"comment"`
}
```
### 98 register_by_email
//const  "**retrieve**":"register_by_email"
```
type register_req struct {
	NickName  string `json:"nick_name"`
	Email     string `json:"email"`
	Password  string `json:"password"`
	PinCode   string `json:"pin_code"`
	DeviceId  string `json:"device_id"`
	PublicKey string `json:"public_key"`
	Pushid    string `json:"pushid"`
	EmailCode string `json:"email_code"`
}

type register_resp struct {
	NickName string `json:"nick_name"`
	UserNo   string `json:"user_no"`
	Retrieve string `json:"retrieve"`
	Seq      string `json:"seq"`
	Result   int    `json:"result"`
	Comment  string `json:"comment"`
}
```
### 99 login_by_email
//const  "**retrieve**":"login_by_email"
### 100 login_by_email_password
//const  "**retrieve**":"login_by_email_password"
### 101 login_by_email_google_code
//const  "**retrieve**":"login_by_email_google_code"
```
type login_req struct {
	Email      string `json:"email"`
	Password   string `json:"password"` // when use email, use this.
	Nonce      string `json:"nonce"`
	ClientType string `json:"client_type"`
	CaptchaId  string `json:"captcha_id"`
	DeviceId   string `json:"device_id"`
	OpenId     string `json:"open_id"`
	UserNo     string `json:"user_no"`
	PinCode    string `json:"pin_code"`   //optional for auto register
	PublicKey  string `json:"public_key"` //optional for auto register
	Pushid     string `json:"pushid"`     //optional for auto register
	GoogleCode string `json:"google_code"`
	EmailCode  string `json:"email_code"`
}

type login_resp struct {
	NickName    string               `json:"nick_name"`
	UserNo      string               `json:"user_no"`
	Logoid      string               `json:"logoid"`
	Assets      []*iproto.UserAssets `json:"assets"`
	TotalGz     string               `json:"total_gz"`   //added
	TotalUsdt   string               `json:"total_usdt"` //added
	Token       string               `json:"token"`
	KycStatus   string               `json:"kyc_status"`
	BioEnable   string               `json:"bio_enable"`
	SmsEnable   string               `json:"sms_enable"`
	TwofaEnable string               `json:"twofa_enable"` //DISABLED,ENABLED,BINDED
	Retrieve    string               `json:"retrieve"`
	Seq         string               `json:"seq"`
	Result      reterr.ErrCode       `json:"result"`
	Comment     string               `json:"comment"`
}
```
### 102 change_password_by_email
//const  "**retrieve**":"change_password_by_email"
```
```
### 103 get_google_code_by_email
//const  "**retrieve**":"get_google_code_by_email"
```
type get_google_code_by_email_req struct {
	EmailCode string `json:"email_code"` //required when bind again
}
type get_google_code_by_email_resp struct {
	QrCode   string `json:"qr_code"`
	Secret   string `json:"secret"`
	Retrieve string `json:"retrieve"`
	Seq      string `json:"seq"`
	Result   int    `json:"result"`
	Comment  string `json:"comment"`
}
```
### 104 bind_google_code_by_email
//const  "**retrieve**":"bind_google_code_by_email"
```
type bind_google_code_by_email_req struct {
	EmailCode  string `json:"email_code"`
	Secret     string `json:"secret"` //if secret is empty, will clear the binding
	GoogleCode string `json:"google_code"`
}
type bind_google_code_by_email_resp struct {
	Retrieve string `json:"retrieve"`
	Seq      string `json:"seq"`
	Result   int    `json:"result"`
	Comment  string `json:"comment"`
}
```
### 105 enable_google_code_by_email
//const  "**retrieve**":"enable_google_code_by_email"
```
type enable_google_code_by_email_req struct {
	EmailCode  string `json:"email_code"`
	GoogleCode string `json:"google_code"`
	Enable     string `json:"enable"` //DISABLED,ENABLED
}
type enable_google_code_by_email_resp struct {
	Retrieve string `json:"retrieve"`
	Seq      string `json:"seq"`
	Result   int    `json:"result"`
	Comment  string `json:"comment"`
}
```
### 106 submit_payment_by_sms
//const  "**retrieve**":"submit_payment_by_sms"
```
type submit_payment_request struct {
	AssetName     string `json:"asset_name"`
	Amount        string `json:"amount"`
	FromPhone     string `json:"from_phone"`
	FromPhoneCode string `json:"from_phone_code"`
	FeePaidBy     string `json:"fee_paid_by"`   // "FROM","TO", empty default "FROM"
	OrderId       string `json:"order_id"`      // order id from merchant
	ToPhone       string `json:"to_phone"`      // reciever
	ToPhoneCode   string `json:"to_phone_code"` // reciever
	Merchantid    string `json:"merchantid"`
	MerchantName  string `json:"merchant_name"`
	SmsCode       string `json:"sms_code"`
	PinCode       string `json:"pin_code"`
}

type submit_payment_response struct {
	Id  string `json:"id"`  // system order id
	Url string `json:"url"` // system payment url , used by merchant, redirect to user

	AssetName     string `json:"asset_name"`
	Amount        string `json:"amount"`
	FromPhone     string `json:"from_phone"`
	FromPhoneCode string `json:"from_phone_code"`

	Fee       string `json:"fee"`         // denominated by AssetName
	FeePaidBy string `json:"fee_paid_by"` // "FROM","TO", empty default "FROM"

	OrderId      string `json:"order_id"`      // order id from merchant
	ToPhone      string `json:"to_phone"`      // reciever
	ToPhoneCode  string `json:"to_phone_code"` // reciever
	Merchantid   string `json:"merchantid"`
	MerchantName string `json:"merchant_name"`
	Retrieve     string `json:"retrieve"`
	Seq          string `json:"seq"`
	Result       int    `json:"result"`
	Comment      string `json:"comment"`
}
```
### 107 payment_setting
//const  "**retrieve**":"payment_setting"
```
type payment_setting_request struct {
	PaymentSetting string `json:"payment_setting"` //BY_PINCODE,BY_PIN_SMS_GOOGLE_CODE,BY_GOOGLE_CODE
}

type payment_setting_response struct {
	PaymentSetting string `json:"payment_setting"`
	Retrieve       string `json:"retrieve"`
	Seq            string `json:"seq"`
	Result         int    `json:"result"`
	Comment        string `json:"comment"`
}
```
### 108 check_pin_code
//const  "**retrieve**":"check_pin_code"
```
type check_pincode_request struct {
	PinCode string `json:"pin_code"`
}
type check_pincode_response struct {
	Retrieve string         `json:"retrieve"`
	Seq      string         `json:"seq"`
	Result   reterr.ErrCode `json:"result"`
	Comment  string         `json:"comment"`
}
```
## Oauth
### 2001 uat urls
request url:
step1: http://18.162.245.23:8666/oauth/register
step2: http://18.162.245.23:8666/oauth/login
step3: http://18.162.245.23:8666/oauth/auth
step4: http://18.162.245.23:8666/oauth/authorize?client_id=GZWallet&response_type=code&scope=all&state=xyz
//client_id use your appid here.
resp:
http://18.162.245.23:8666/oauth/authorize?code=WVTIZN_FPRMPEU0GLDEBEQ&state=xyz

step5: 
//const  "**retrieve**":"oauth_authorize" 
```
type retrieve_request struct {
	Appid     string      `json:"appid"`
	Sign      string      `json:"sign"`
	SignType  string      `json:"sign_type"`
	Retrieve string      `json:"retrieve"`
	Data     interface{} `json:"data"`
	Seq        string   `json:"seq"`
}
type oauth_authorize_req struct {
	AuthorizeUrl string `json:"authorize_url"`
	ClientId     string `json:"client_id"`
	Code         string `json:"code"`          //provide the responsed code above
	RedirectUrl  string `json:"redirect_url"`  //leave empty, step5 do not use redirect_url
	ResponseType string `json:"response_type"` //leave empty
	Scope        string `json:"scope"`         //leave empty
	State        string `json:"state"`         //leave empty
}
type oauth_authorize_resp struct {
	OpenId   string         `json:"openid"`    //use this openid to login_xpp,can exprie
	Retrieve string         `json:"retrieve"`
	Seq      string         `json:"seq"`
	Result   reterr.ErrCode `json:"result"`
	Comment  string         `json:"comment"`
}
```
### 2002 refresh_openid
//const  "**retrieve**":"oauth_refresh_openid" 
```
type retrieve_request struct {
	Appid     string      `json:"appid"`
	Sign      string      `json:"sign"`
	SignType  string      `json:"sign_type"`
	Retrieve string      `json:"retrieve"`
	Data     interface{} `json:"data"`
	Seq        string   `json:"seq"`
}
type oauth_refresh_openid_req struct {
	Openid string `json:"openid"`
}

type oauth_refresh_openid_resp struct {
	Openid   string         `json:"openid"`
	Retrieve string         `json:"retrieve"`
	Seq      string         `json:"seq"`
	Result   reterr.ErrCode `json:"result"`
	Comment  string         `json:"comment"`
}

```
### 2003 get_openid
//const  "**retrieve**":"get_openid" 
```
type get_openid_resp struct {
	Openid   string         `json:"openid"`
	Retrieve string         `json:"retrieve"`
	Seq      string         `json:"seq"`
	Result   reterr.ErrCode `json:"result"`
	Comment  string         `json:"comment"`
}
```
### 2004 close user
//const  "**retrieve**":"close_user" 
```
type close_user_req struct {
	/*
		Deleted    = 1;
		Closed     = 3;
		Frozen     = 4;
	*/
	Status int32 `json:"status"`
}
type close_user_resp struct {
	Status   int32  `json:"status"`
	Retrieve string `json:"retrieve"`
	Seq      string `json:"seq"`
	Result   int    `json:"result"`
	Comment  string `json:"comment"`
}
```

## Admin
### 1001 register
//const  "**method**":"register"
```
type retrieve_request struct {
	Appid     string      `json:"appid"` // for example: GZWallet
	Sign      string      `json:"sign"`  // using signature alg mentioned next page
	SignType  string      `json:"sign_type"` // const "SHA256withRSA"
	Name      string      `json:"name"`  // ensure only admin can derive account
	Token     string      `json:"token"`
	Method    string      `json:"method"`
	Data      interface{} `json:"data"`
}
type register_req struct {
	Name     string `json:"name"`
	Password string `json:"password"`
}

type register_resp struct {
	Name     string `json:"name"`
	Retrieve string `json:"retrieve"`
	Seq      string `json:"seq"`
	Result   int    `json:"result"`
	Comment  string `json:"comment"`
}
```
### 1002 login
//const  "**method**":"login"
```
type retrieve_request struct {
	Appid     string      `json:"appid"` // for example: GZWallet
	Sign      string      `json:"sign"`  // using signature alg mentioned next page
	SignType  string      `json:"sign_type"` // const "SHA256withRSA"
	Method    string      `json:"method"`
	Data      interface{} `json:"data"`
}

type login_req struct {
	Name       string `json:"name"`
	Nonce      string `json:"nonce"`
	ClientType string `json:"client_type"`
	CaptchaId  string `json:"captcha_id"`
	Password   string `json:"password"`
	GoogleCode string `json:"google_code"`
}

type login_resp struct {
	Appid      string          `json:"appid"`
	Merchantid string          `json:"merchantid"`
	Name       string          `json:"name"`
	Power      string          `json:"power"`
	Rights     *iproto.Rrights `json:"rights"`// described as in ### 1092
	Token      string          `json:"token"`
	QrCode     string          `json:"qr_code"`//when result=95,use this to bind 2fa
	Secret     string          `json:"secret"` //when result=95,use this to bind 2fa
	Retrieve   string          `json:"retrieve"`
	Seq        string          `json:"seq"`
	Result     reterr.ErrCode  `json:"result"`
	Comment    string          `json:"comment"`
}
```
### 1002.1 login_by_google_code
//const  "**method**":"login_by_google_code"
```
type login_req struct {
	Name       string `json:"name"`
	Nonce      string `json:"nonce"`
	ClientType string `json:"client_type"`
	CaptchaId  string `json:"captcha_id"`
	Password   string `json:"password"`
	Secret     string `json:"secret"`
	GoogleCode string `json:"google_code"`
}

type login_resp struct {
	Appid      string          `json:"appid"`
	Merchantid string          `json:"merchantid"`
	Name       string          `json:"name"`
	Power      string          `json:"power"`
	Rights     *iproto.Rrights `json:"rights"`
	Token      string          `json:"token"`
	QrCode     string          `json:"qr_code"`
	Secret     string          `json:"secret"`
	Retrieve   string          `json:"retrieve"`
	Seq        string          `json:"seq"`
	Result     reterr.ErrCode  `json:"result"`
	Comment    string          `json:"comment"`
}
```
### 1003 refresh_token
//const  "**method**":"refresh_token"
```
type retrieve_request struct {
	Appid     string      `json:"appid"` // for example: GZWallet
	Sign      string      `json:"sign"`  // using signature alg mentioned next page
	SignType  string      `json:"sign_type"` // const "SHA256withRSA"
	Name      string      `json:"name"`
	Token     string      `json:"token"`
	Method    string      `json:"method"`
	Data      interface{} `json:"data"`
}

type refresh_req struct {
}

type refresh_resp struct {
	AccessToken  string         `json:"access_token"`
	RefreshToken string         `json:"refresh_token"`
	TokenType    string         `json:"token_type"`
	Expires      int64          `json:"expires"`
	Retrieve     string         `json:"retrieve"`
	Seq          string         `json:"seq"`
	Result       reterr.ErrCode `json:"result"`
	Comment      string         `json:"comment"`
}
```
### 1004 reset_password
//const  "**method**":"reset_password"
```
type retrieve_request struct {
	Appid     string      `json:"appid"` // for example: GZWallet
	Sign      string      `json:"sign"`  // using signature alg mentioned next page
	SignType  string      `json:"sign_type"` // const "SHA256withRSA"
	Name      string      `json:"name"`
	Token     string      `json:"token"`
	Method    string      `json:"method"`
	Data      interface{} `json:"data"`
}

type reset_psw_req struct { // for admin use only
	Appid       string `json:"appid"`
	Name        string `json:"name"`
	NewPassword string `json:"new_password"`
}

type reset_psw_resp struct {
	Appid       string         `json:"appid"`
	Name        string         `json:"name"`
	NewPassword string         `json:"new_password"`
	Retrieve    string         `json:"retrieve"`
	Seq         string         `json:"seq"`
	Result      reterr.ErrCode `json:"result"`
	Comment     string         `json:"comment"`
}
```
### 1005 add roles
//const  "**method**":"add_role"
```
type retrieve_request struct {
	Appid     string      `json:"appid"` // for example: GZWallet
	Sign      string      `json:"sign"`  // using signature alg mentioned next page
	SignType  string      `json:"sign_type"` // const "SHA256withRSA"
	Name      string      `json:"name"`
	Token     string      `json:"token"`
	Method    string      `json:"method"`
	Data      interface{} `json:"data"`
}

type add_roles_req struct {
	Appid  string `json:"appid"`
	Name   string `json:"name"`
	Power  string `json:"power"`
	Status string `json:"status"`
}

type add_roles_resp struct {
	Appid    string `json:"appid"`
	Name     string `json:"name"`
	Power    string `json:"power"`
	Status   string `json:"status"`
	Retrieve string `json:"retrieve"`
	Seq      string `json:"seq"`
	Result   int    `json:"result"`
	Comment  string `json:"comment"`
}
```
### 1006 update roles
//const  "**method**":"update_role"
```
type retrieve_request struct {
	Appid     string      `json:"appid"` // for example: GZWallet
	Sign      string      `json:"sign"`  // using signature alg mentioned next page
	SignType  string      `json:"sign_type"` // const "SHA256withRSA"
	Name      string      `json:"name"`
	Token     string      `json:"token"`
	Method    string      `json:"method"`
	Data      interface{} `json:"data"`
}

type update_roles_req struct {
	Appid  string `json:"appid"`
	Name   string `json:"name"`
	Power  string `json:"power"`
	Status string `json:"status"`
}

type update_roles_resp struct {
	Appid    string `json:"appid"`
	Name     string `json:"name"`
	Power    string `json:"power"`
	Status   string `json:"status"`
	Retrieve string `json:"retrieve"`
	Seq      string `json:"seq"`
	Result   int    `json:"result"`
	Comment  string `json:"comment"`
}
```
### 1007  roles list
//const  "**method**":"roles_list"
```
type retrieve_request struct {
	Appid     string      `json:"appid"` // for example: GZWallet
	Sign      string      `json:"sign"`  // using signature alg mentioned next page
	SignType  string      `json:"sign_type"` // const "SHA256withRSA"
	Name      string      `json:"name"`
	Token     string      `json:"token"`
	Method    string      `json:"method"`
	Data      interface{} `json:"data"`
}

type roles_list_req struct {
	Appid      string `json:"appid"`
	PageNumber int64  `json:"page_number"`
	PageSize   int64  `json:"page_size"`
}

type roles_list_resp struct {
	Appid      string         `json:"appid"`
	RoleNames  []iproto.Roles `json:"role_names"`
	PageNumber int64          `json:"page_number"`
	PageSize   int64          `json:"page_size"`
	Total      int64          `json:"total"`
	Retrieve   string         `json:"retrieve"`
	Seq        string         `json:"seq"`
	Result     int            `json:"result"`
	Comment    string         `json:"comment"`
}
type iAdminRoles struct {
	Appid      string          `json:"appid"`
	Name       string          `json:"name"`
	Power      string          `json:"power"`
	Rights     *iproto.Rrights `json:"rights"`
	CreateTime string          `json:"create_time"`
	UpdateTime string          `json:"update_time"`
	CreatedBy  string          `json:"created_by"`
	UpdatedBy  string          `json:"updated_by"`
	Status     string          `json:"status"`
}
type iroles_list_resp struct {
	Appid      string         `json:"appid"`
	RoleNames  []*iAdminRoles `json:"role_names"`
	PageNumber int64          `json:"page_number"`
	PageSize   int64          `json:"page_size"`
	Total      int64          `json:"total"`
	Retrieve   string         `json:"retrieve"`
	Seq        string         `json:"seq"`
	Result     int            `json:"result"`
	Comment    string         `json:"comment"`
}
```
### 1008  update_admin_roles
//const  "**method**":"update_admin_roles"
```
type retrieve_request struct {
	Appid     string      `json:"appid"` // for example: GZWallet
	Sign      string      `json:"sign"`  // using signature alg mentioned next page
	SignType  string      `json:"sign_type"` // const "SHA256withRSA"
	Name      string      `json:"name"`
	Token     string      `json:"token"`
	Method    string      `json:"method"`
	Data      interface{} `json:"data"`
}

type update_admin_roles_req struct {
	Appid     string   `json:"appid"`
	AdminName string   `json:"admin_name"`
	RoleNames []string `json:"role_names"`
}

type update_admin_roles_resp struct {
	Appid     string   `json:"appid"`
	AdminName string   `json:"admin_name"`
	RoleNames []string `json:"role_names"`
	Retrieve  string   `json:"retrieve"`
	Seq       string   `json:"seq"`
	Result    int      `json:"result"`
	Comment   string   `json:"comment"`
}
```
### 1009 role_config_list
//TO BE DELETE
//const  "**method**":"role_config_list"
```
type role_config_list_req struct {
	Appid     string      `json:"appid"` // for example: GZWallet
	Sign      string      `json:"sign"`  // using signature alg mentioned next page
	SignType  string      `json:"sign_type"` // const "SHA256withRSA"
	PageNumber int64 `json:"page_number"`
	PageSize   int64 `json:"page_size"`
}

type role_config_list_resp struct {
	Configs    map[int32]string `json:"configs"`
	Total      int64            `json:"total"`
	PageNumber int64            `json:"page_number"`
	PageSize   int64            `json:"page_size"`
	Retrieve   string           `json:"retrieve"`
	Seq        string           `json:"seq"`
	Result     int              `json:"result"`
	Comment    string           `json:"comment"`
}
```
### 1010 logout
//const  "**retrieve**":"logout"
```
type retrieve_request struct {
	Appid     string      `json:"appid"` // for example: GZWallet
	Sign      string      `json:"sign"`  // using signature alg mentioned next page
	SignType  string      `json:"sign_type"` // const "SHA256withRSA"
	Name      string      `json:"name"`
	Token     string      `json:"token"`
	Method    string      `json:"method"`
	Seq        string   `json:"seq"`
	Data      interface{} `json:"data"`
}
type logout_req struct {
}

type logout_resp struct {
	Retrieve string         `json:"retrieve"`
	Seq      string         `json:"seq"`
	Result   reterr.ErrCode `json:"result"`
	Comment  string         `json:"comment"`
}
```
### 1011 login_by_token
//const  "**method**":"login_by_token"
```
type retrieve_request struct {
	Appid     string      `json:"appid"` // for example: GZWallet
	Sign      string      `json:"sign"`  // using signature alg mentioned next page
	SignType  string      `json:"sign_type"` // const "SHA256withRSA"
	Name      string      `json:"name"`
	Token     string      `json:"token"`
	Method    string      `json:"method"`
	Data      interface{} `json:"data"`
}
type login_req struct {
}

type login_resp struct {
	Name     string         `json:"name"`
	Power    string         `json:"power"`
	Token    string         `json:"token"`
	Retrieve string         `json:"retrieve"`
	Seq      string         `json:"seq"`
	Result   int            `json:"result"`
	Comment  string         `json:"comment"`
}
```
###1012 user_list
//const  "**method**":"user_list"
```
type retrieve_request struct {
	Appid     string      `json:"appid"` // for example: GZWallet
	Sign      string      `json:"sign"`  // using signature alg mentioned next page
	SignType  string      `json:"sign_type"` // const "SHA256withRSA"
	Name      string      `json:"name"`
	Token     string      `json:"token"`
	Method    string      `json:"method"`
	Data      interface{} `json:"data"`
}
type user_list_req struct { // these are filters
	Appid      string `json:"appid"`
	Phone      string `json:"phone"`
	PhoneCode  string `json:"phone_code"`
	StartTime  int64  `json:"start_time"`
	EndTime    int64  `json:"end_time"`
	Status     string `json:"status"`  // empty("") for all, use "0","1","2" , meaning "Normal","Deleted","Inactivated".
	PageNumber int64  `json:"page_number"`
	PageSize   int64  `json:"page_size"`
}
type Users struct {
	Id                   string        `json:"id"`
	Appid                string        `json:"appid"`
	Name                 string        `json:"name"`
	Password             []byte        `json:"password"`
	Phone                string        `json:"phone"`
	PhoneCode            string        `json:"phone_code"`
	Type                 UsersEt       `json:"type"`
	NickName             string        `json:"nick_name"`
	Status               int32         `json:"status"`
	PinCode              []byte        `json:"pin_code"`
	AreaDistricts        string        `json:"area_districts"`
	Email                string        `json:"email"`
	Gender               string        `json:"gender"`
	Birthday             string        `json:"birthday"`
	CreateTime           string        `json:"create_time"`
	UpdateTime           string        `json:"update_time"`
	Logoid               string        `json:"logoid"`
	Vid                  uint64        `json:"vid"`
	RoleNames            []string      `json:"role_names"`
	CreatedBy            string        `json:"created_by"`
	UpdatedBy            string        `json:"updated_by"`
	KycStatus            string        `json:"kyc_status"`
	Assets               []*UserAssets `json:"assets"`
	RegisterFrom         string        `json:"register_from"`
}
type user_list_resp struct {
	Users      []iproto.Users `json:"users"`
	Appid      string         `json:"appid"`
	Phone      string         `json:"phone"`
	PhoneCode  string         `json:"phone_code"`
	Status     string         `json:"status"`
	StartTime  int64          `json:"start_time"`
	EndTime    int64          `json:"end_time"`
	Total      int64          `json:"total"`
	PageNumber int64          `json:"page_number"`
	PageSize   int64          `json:"page_size"`
	Retrieve   string         `json:"retrieve"`
	Seq        string         `json:"seq"`
	Result     int            `json:"result"`
	Comment    string         `json:"comment"`
}

```
### 1013 admin_list
//const  "**method**":"admin_list"
```
type retrieve_request struct {
	Appid     string      `json:"appid"` // for example: GZWallet
	Sign      string      `json:"sign"`  // using signature alg mentioned next page
	SignType  string      `json:"sign_type"` // const "SHA256withRSA"
	Name      string      `json:"name"`
	Token     string      `json:"token"`
	Method    string      `json:"method"`
	Data      interface{} `json:"data"`
}
type admin_list_req struct {
	Appid      string `json:"appid"`
	StartTime  int64  `json:"start_time"`
	EndTime    int64  `json:"end_time"`
	Status     string `json:"status"`//status_config_list :  "STATUS_NORMAL", "STATUS_DISABLE", "STATUS_DELETED"
	PageNumber int64  `json:"page_number"`
	PageSize   int64  `json:"page_size"`
}
type iAdmins struct {
	Id             string   `json:"id"`
	Appid          string   `json:"appid"`
	Status         string   `json:"status"`
	CreateTime     string   `json:"create_time"`
	UpdateTime     string   `json:"update_time"`
	CreatedBy      string   `json:"created_by"`
	UpdatedBy      string   `json:"updated_by"`
	RoleNames      []string `json:"role_names"`
	LastLoginTime  string   `json:"last_login_time"`
	LastLogoutTime string   `json:"last_logout_time"`
}
type admin_list_resp struct {
	Admins     []iproto.Admins `json:"admins"`
	Appid      string          `json:"appid"`
	Status     string          `json:"status"`
	StartTime  int64           `json:"start_time"`
	EndTime    int64           `json:"end_time"`
	Total      int64           `json:"total"`
	PageNumber int64           `json:"page_number"`
	PageSize   int64           `json:"page_size"`
	Retrieve   string          `json:"retrieve"`
	Seq        string          `json:"seq"`
	Result     int             `json:"result"`
	Comment    string          `json:"comment"`
}
```
### 1014 update_admin_user
//const  "**method**":"update_admin_user"
```
type retrieve_request struct {
	Appid     string      `json:"appid"` // for example: GZWallet
	Sign      string      `json:"sign"`  // using signature alg mentioned next page
	SignType  string      `json:"sign_type"` // const "SHA256withRSA"
	Name      string      `json:"name"`
	Token     string      `json:"token"`
	Method    string      `json:"method"`
	Data      interface{} `json:"data"`
}

type update_admin_user_req struct {
	AdminName string `json:"admin_name"`
	Appid     string `json:"appid"` // leave empty here
	Status    string `json:"status"` // STATUS_NORMAL,STATUS_DISABLE,STATUS_DELETED
}

type update_admin_user_resp struct {
	AdminName string `json:"admin_name"`
	Appid     string `json:"appid"`
	Status    string `json:"status"`
	Retrieve  string `json:"retrieve"`
	Seq       string `json:"seq"`
	Result    int    `json:"result"`
	Comment   string `json:"comment"`
}
```
### 1015 app_user_add
//const  "**method**":"app_user_add"
```
type retrieve_request struct {
	Appid     string      `json:"appid"` // for example: GZWallet
	Sign      string      `json:"sign"`  // using signature alg mentioned next page
	SignType  string      `json:"sign_type"` // const "SHA256withRSA"
	Name      string      `json:"name"`
	Token     string      `json:"token"`
	Method    string      `json:"method"`
	Data      interface{} `json:"data"`
}

type add_appuser_req struct {
	PhoneCode        string `json:"phone_code"`
	Phone            string `json:"phone"`
	User             string `json:"user"`
	UserNo           string `json:"user_no"`
	Appid            string `json:"appid"`
	Pubkey           string `json:"pubkey"`
	Asset            string `json:"asset"`
	Type             string `json:"type"`// const TYPE_INITIAL
	SmsRequire       string `json:"sms_require"`// YES,NO
	AssetCallbackUrl string `json:"asset_callback_url"`
	AuthRequire      string `json:"auth_require"`// YES,NO
	IsInvestor       string `json:"is_investor"`// YES,NO
	Status           string `json:"status"`// STATUS_NORMAL,STATUS_DISABLE,STATUS_DELETED
	PaymentUrl       string `json:"payment_url"`
	FrozenUrl        string `json:"frozen_url"`
	AssetAddressUrl  string `json:"asset_address_url"`
	QueryCallbackUrl string `json:"query_callback_url"`
	SmsTag           string `json:"sms_tag"`
	ReportPsw        string `json:"report_psw"`
	BindUrl          string `json:"bind_url"`
	Md5key           string `json:"md5key"`
	SiteUrl          string   `json:"site_url"`
	Name             string   `json:"name"`
	ConfirmUrl       string   `json:"confirm_url"`
}

type add_appuser_resp struct {
	PhoneCode        string `json:"phone_code"`
	Phone            string `json:"phone"`
	User             string `json:"user"`
	Appid            string `json:"appid"`
	Pubkey           string `json:"pubkey"`
	Asset            string `json:"asset"`
	Type             string `json:"type"`
	SmsRequire       string `json:"sms_require"`
	AssetCallbackUrl string `json:"asset_callback_url"`
	AuthRequire      string `json:"auth_require"`
	IsInvestor       string `json:"is_investor"`
	Status           string `json:"status"`
	PaymentUrl       string `json:"payment_url"`
	FrozenUrl        string `json:"frozen_url"`
	AssetAddressUrl  string `json:"asset_address_url"`
	QueryCallbackUrl string `json:"query_callback_url"`
	SmsTag           string `json:"sms_tag"`
	ReportPsw        string `json:"report_psw"`
	BindUrl          string `json:"bind_url"`
	Md5key           string `json:"md5key"`
	SiteUrl          string   `json:"site_url"`
	Name             string   `json:"name"`
	ConfirmUrl       string   `json:"confirm_url"`
	Retrieve         string `json:"retrieve"`
	Seq              string `json:"seq"`
	Result           int    `json:"result"`
	Comment          string `json:"comment"`
}
```
### 1016 app_user_update
//const  "**method**":"app_user_update"
```
type retrieve_request struct {
	Appid     string      `json:"appid"` // for example: GZWallet
	Sign      string      `json:"sign"`  // using signature alg mentioned next page
	SignType  string      `json:"sign_type"` // const "SHA256withRSA"
	Name      string      `json:"name"`
	Token     string      `json:"token"`
	Method    string      `json:"method"`
	Data      interface{} `json:"data"`
}

type update_appuser_req struct {
	PhoneCode        string `json:"phone_code"`
	Phone            string `json:"phone"`
	User             string `json:"user"`
	UserNo           string `json:"user_no"`
	Appid            string `json:"appid"`
	Pubkey           string `json:"pubkey"`
	Asset            string `json:"asset"`
	Type             string `json:"type"`
	SmsRequire       string `json:"sms_require"`
	AssetCallbackUrl string `json:"asset_callback_url"`
	AuthRequire      string `json:"auth_require"`
	IsInvestor       string `json:"is_investor"`
	Status           string `json:"status"`
	PaymentUrl       string `json:"payment_url"`
	FrozenUrl        string `json:"frozen_url"`
	AssetAddressUrl  string `json:"asset_address_url"`
	QueryCallbackUrl string `json:"query_callback_url"`
	SmsTag           string `json:"sms_tag"`
	ReportPsw        string `json:"report_psw"`
	BindUrl          string `json:"bind_url"`
	Md5key           string `json:"md5key"`
	SiteUrl          string   `json:"site_url"`
	Name             string   `json:"name"`
	ConfirmUrl       string   `json:"confirm_url"`
}

type update_appuser_resp struct {
	PhoneCode        string `json:"phone_code"`
	Phone            string `json:"phone"`
	User             string `json:"user"`
	Appid            string `json:"appid"`
	Pubkey           string `json:"pubkey"`
	Asset            string `json:"asset"`
	Type             string `json:"type"`
	SmsRequire       string `json:"sms_require"`
	AssetCallbackUrl string `json:"asset_callback_url"`
	AuthRequire      string `json:"auth_require"`
	IsInvestor       string `json:"is_investor"`
	Status           string `json:"status"`
	PaymentUrl       string `json:"payment_url"`
	FrozenUrl        string `json:"frozen_url"`
	AssetAddressUrl  string `json:"asset_address_url"`
	QueryCallbackUrl string `json:"query_callback_url"`
	SmsTag           string `json:"sms_tag"`
	ReportPsw        string `json:"report_psw"`
	BindUrl          string `json:"bind_url"`
	Md5key           string `json:"md5key"`
	SiteUrl          string   `json:"site_url"`
	Name             string   `json:"name"`
	ConfirmUrl       string   `json:"confirm_url"`
	Retrieve         string `json:"retrieve"`
	Seq              string `json:"seq"`
	Result           int    `json:"result"`
	Comment          string `json:"comment"`
}
```
### 1017 app_user_list
//const  "**method**":"app_user_list"
```
type retrieve_request struct {
	Appid     string      `json:"appid"` // for example: GZWallet
	Sign      string      `json:"sign"`  // using signature alg mentioned next page
	SignType  string      `json:"sign_type"` // const "SHA256withRSA"
	Name      string      `json:"name"`
	Token     string      `json:"token"`
	Method    string      `json:"method"`
	Data      interface{} `json:"data"`
}
type appuser_list_req struct {
	Appid      string `json:"appid"`
	Phone      string `json:"phone"`
	PhoneCode  string `json:"phone_code"`
	StartTime  int64  `json:"start_time"`
	EndTime    int64  `json:"end_time"`
	Status     string `json:"status"`
	PageNumber int64  `json:"page_number"`
	PageSize   int64  `json:"page_size"`
}

type appuser_list_resp struct {
	List       []iAppUsers `json:"list"`
	Appid      string      `json:"appid"`
	Phone      string      `json:"phone"`
	PhoneCode  string      `json:"phone_code"`
	StartTime  int64       `json:"start_time"`
	EndTime    int64       `json:"end_time"`
	Status     string      `json:"status"`
	PageNumber int64       `json:"page_number"`
	PageSize   int64       `json:"page_size"`
	Total      int64       `json:"total"`
	Retrieve   string      `json:"retrieve"`
	Seq        string      `json:"seq"`
	Result     int         `json:"result"`
	Comment    string      `json:"comment"`
}
```
### 1018.0 report here
**with suffix 'xls', the request is the same as in suffix of 'list'**
**suffix 'xls' and 'list' both valid in rpc and ws url**
//const  "**method**": "withdraw_xls"
//const  "**method**": "transfer_xls"
//const  "**method**": "payment_xls"
//const  "**method**": "deposit_xls"
**use the url in the response to download statement file**
dev:
super&admin:
https://reportscsv-dev.s3.ap-east-1.amazonaws.com/all-userlist-20200512.zip
https://reportscsv-dev.s3.ap-east-1.amazonaws.com/all-transfer-20200528.zip
https://reportscsv-dev.s3.ap-east-1.amazonaws.com/all-payment-20200528.zip
https://reportscsv-dev.s3.ap-east-1.amazonaws.com/all-withdraw-20200528.zip
https://reportscsv-dev.s3.ap-east-1.amazonaws.com/all-deposit-20200528.zip
https://reportscsv-dev.s3.ap-east-1.amazonaws.com/all-frozen-20200528.zip
https://reportscsv-dev.s3.ap-east-1.amazonaws.com/all-unfrozen-20200528.zip
merchant:
https://reportscsv-dev.s3.ap-east-1.amazonaws.com/bitollmdpay-txlist-20200528.zip
https://reportscsv-dev.s3.ap-east-1.amazonaws.com/bitollmdpay-transfer-20200528.zip
https://reportscsv-dev.s3.ap-east-1.amazonaws.com/bitollmdpay-payment-20200528.zip 
https://reportscsv-dev.s3.ap-east-1.amazonaws.com/bitollmdpay-withdraw-20200528.zip
prd:
https://reportscsv-prd.s3.ap-southeast-1.amazonaws.com/all-userlist-20200512.zip
add/update/list of _appuser/merchant, 增加了一個report_psw
提供一個編輯框填寫即可，長度可以限制比如32
是report下載時的解壓密碼，當前默認密碼：BitollReport2020
7z e  appid-userlist-20200512.zip
用7z解壓，後面這個文件名是用戶資產snapshot規則。20200512是每日的規則
superadmin還可以下載一個 all-userlist-20200512.zip的文件，包含所有的用戶資產快照。
即appid變成了固定的"all" 字串
注意前面的URL, dev&prd不一樣
```
type xls_response struct {
	Url      string `json:"url"`
	Retrieve string `json:"retrieve"`
	Seq      string `json:"seq"`
	Result   int    `json:"result"`
	Comment  string `json:"comment"`
}
```
### 1018 transfer_list
//const  "**method**":"transfer_list"
```
type transfer_list_request struct { // fiters
	Asset         string `json:"asset"`
	Appid         string `json:"appid"`
	FromPhone     string `json:"from_phone"`
	FromPhoneCode string `json:"from_phone_code"`
	ToPhone       string `json:"to_phone"`
	ToPhoneCode   string `json:"to_phone_code"`
	FromUser      string `json:"from_user"`
	FromUserNo    string `json:"from_user_no"`
	ToUser        string `json:"to_user"`
	ToUserNo      string `json:"to_user_no"`
	OrderId       string       `json:"order_id"`
	StartTime     int64  `json:"start_time"`
	EndTime       int64  `json:"end_time"`
	Status        string `json:"status"`
	PageNumber    int64  `json:"page_number"`
	PageSize      int64  `json:"page_size"`
}

type itransfer_list_response struct {
	List          []*wTransfer `json:"list"`
	Asset         string       `json:"asset"`
	Appid         string       `json:"appid"`
	FromPhone     string       `json:"from_phone"`
	FromPhoneCode string       `json:"from_phone_code"`
	ToPhone       string       `json:"to_phone"`
	ToPhoneCode   string       `json:"to_phone_code"`
	FromUser      string       `json:"from_user"`
	FromUserNo    string       `json:"from_user_no"`
	ToUser        string       `json:"to_user"`
	ToUserNo      string       `json:"to_user_no"`
	StartTime     int64        `json:"start_time"`
	EndTime       int64        `json:"end_time"`
	Status        string       `json:"status"`
	PageNumber    int64        `json:"page_number"`
	PageSize      int64        `json:"page_size"`
	Total         int64        `json:"total"`
	Retrieve      string       `json:"retrieve"`
	Seq           string       `json:"seq"`
	Result        int          `json:"result"`
	Comment       string       `json:"comment"`
}

type wTransfer struct {
	Id            string `json:"id"`
	AssetName     string `json:"asset_name"`
	From          string `json:"from"`
	To            string `json:"to"`
	Amount        string `json:"amount"`
	UpdateTime    string `json:"update_time"`
	OrderId       string `json:"order_id"`
	FromPhone     string `json:"from_phone"`
	FromPhoneCode string `json:"from_phone_code"`
	FromUserNo    string `json:"from_user_no"`
	ToPhone       string `json:"to_phone"`
	ToPhoneCode   string `json:"to_phone_code"`
	ToUserNo      string `json:"to_user_no"`
	Status        string `json:"status"`
	Appid         string `json:"appid"`
	RefTransferId string `json:"ref_transfer_id"`
	CreateTime    string `json:"create_time"`
	Fee           string `json:"fee"`
	FeePaidBy     string `json:"fee_paid_by"`
	PaidTotal     string `json:"paid_total"`
	FromFromBalance string `json:"from_from_balance"`
	FromFromFrozen  string `json:"from_from_frozen"`
	FromToBalance   string `json:"from_to_balance"`
	FromToFrozen    string `json:"from_to_frozen"`
	ToFromBalance   string `json:"to_from_balance"`
	ToFromFrozen    string `json:"to_from_frozen"`
	ToToBalance     string `json:"to_to_balance"`
	ToToFrozen      string `json:"to_to_frozen"`
	AcceptedFrom    string `json:"accepted_from"`
	ReturnRefid     string `json:"return_refid"`
}
```
### 1018.0 merchant_transfer_list
//const  "**method**":"merchant_transfer_list"
```
type merchant_transfer_list_request struct { // fiters
	Asset         string `json:"asset"`
	Appid         string `json:"appid"`
	FromPhone     string `json:"from_phone"`
	FromPhoneCode string `json:"from_phone_code"`
	FromUserNo    string `json:"from_user_no"`
	FromUser      string `json:"from_user"`
	ToUser        string `json:"to_user"`
	ToPhone       string `json:"to_phone"`
	ToPhoneCode   string `json:"to_phone_code"`
	ToUserNo      string `json:"to_user_no"`
	ToAddress     string `json:"to_address"`
	OrderId       string       `json:"order_id"`
	StartTime     int64  `json:"start_time"`
	EndTime       int64  `json:"end_time"`
	Status        string `json:"status"`
	PageNumber    int64  `json:"page_number"`
	PageSize      int64  `json:"page_size"`
}

type iTransfer struct {
	Id            string `json:"id"`
	AssetName     string `json:"asset_name"`
	From          string `json:"from"`
	To            string `json:"to"`
	Amount        string `json:"amount"`
	UpdateTime    string `json:"update_time"`
	OrderId       string `json:"order_id"`
	FromPhone     string `json:"from_phone"`
	FromPhoneCode string `json:"from_phone_code"`
	FromUserNo    string `json:"from_user_no"`
	FromUser      string `json:"from_user"`
	ToUser        string `json:"to_user"`
	ToPhone       string `json:"to_phone"`
	ToPhoneCode   string `json:"to_phone_code"`
	ToUserNo      string `json:"to_user_no"`
	ToAddress     string `json:"to_address"`
	Status        string `json:"status"`
	Appid         string `json:"appid"`
	RefTransferId string `json:"ref_transfer_id"`
	CreateTime    string `json:"create_time"`
	Fee           string `json:"fee"`
	FeePaidBy     string `json:"fee_paid_by"`
	PaidTotal     string `json:"paid_total"`
	FromBalance   string `json:"from_balance"`
	FromFrozen    string `json:"from_frozen"`
	ToBalance     string `json:"to_balance"`
	ToFrozen      string `json:"to_frozen"`
	AcceptedFrom  string `json:"accepted_from"`
	Merchantid    string `json:"merchantid"`
	MerchantName  string `json:"merchant_name"`
	ReturnRefid     string `json:"return_refid"`
}
type merchant_transfer_list_response struct {
	List          []*iTransfer `json:"list"`
	Asset         string       `json:"asset"`
	Appid         string       `json:"appid"`
	FromPhone     string       `json:"from_phone"`
	FromPhoneCode string       `json:"from_phone_code"`
	FromUserNo    string       `json:"from_user_no"`
	ToPhone       string       `json:"to_phone"`
	ToPhoneCode   string       `json:"to_phone_code"`
	ToUserNo      string       `json:"to_user_no"`
	ToAddress     string       `json:"to_address"`
	StartTime     int64        `json:"start_time"`
	EndTime       int64        `json:"end_time"`
	Status        string       `json:"status"`
	PageNumber    int64        `json:"page_number"`
	PageSize      int64        `json:"page_size"`
	Total         int64        `json:"total"`
	Retrieve      string       `json:"retrieve"`
	Seq           string       `json:"seq"`
	Result        int          `json:"result"`
	Comment       string       `json:"comment"`
}
```
### 1019 payment_list
//const  "**method**":"payment_list"
//for superadmin&admin
```
type payment_list_request struct { // fiters
	Asset         string `json:"asset"`
	Appid         string `json:"appid"`
	FromPhone     string `json:"from_phone"`
	FromPhoneCode string `json:"from_phone_code"`
	ToPhone       string `json:"to_phone"`
	ToPhoneCode   string `json:"to_phone_code"`
	FromUser      string `json:"from_user"`
	FromUserNo    string `json:"from_user_no"`
	ToUser        string `json:"to_user"`
	ToUserNo      string `json:"to_user_no"`
	OrderId       string       `json:"order_id"`
	StartTime     int64  `json:"start_time"`
	EndTime       int64  `json:"end_time"`
	Status        string `json:"status"`
	PageNumber    int64  `json:"page_number"`
	PageSize      int64  `json:"page_size"`
}
type wPayments struct {
	Id              string `json:"id"`
	Appid           string `json:"appid"`
	AssetName       string `json:"asset_name"`
	Amount          string `json:"amount"`
	Fee             string `json:"fee"`
	From            string `json:"from"`
	FromUser        string `json:"from_user"`
	FromPhone       string `json:"from_phone"`
	FromPhoneCode   string `json:"from_phone_code"`
	FromUserNo      string `json:"from_user_no"`
	To              string `json:"to"`
	ToUser          string `json:"to_user"`
	ToPhone         string `json:"to_phone"`
	ToPhoneCode     string `json:"to_phone_code"`
	ToUserNo        string `json:"to_user_no"`
	OrderId         string `json:"order_id"`
	FeePaidBy       string `json:"fee_paid_by"`
	CallbackUrl     string `json:"callback_url"`
	RedirectUrl     string `json:"redirect_url"`
	CreateTime      string `json:"create_time"`
	UpdateTime      string `json:"update_time"`
	Status          string `json:"status"`
	PaidTotal       string `json:"paid_total"`
	FromFromBalance string `json:"from_from_balance"`
	FromFromFrozen  string `json:"from_from_frozen"`
	FromToBalance   string `json:"from_to_balance"`
	FromToFrozen    string `json:"from_to_frozen"`
	ToFromBalance   string `json:"to_from_balance"`
	ToFromFrozen    string `json:"to_from_frozen"`
	ToToBalance     string `json:"to_to_balance"`
	ToToFrozen      string `json:"to_to_frozen"`
	AcceptedFrom    string `json:"accepted_from"`
	ReturnRefid     string `json:"return_refid"`
}
type ipayment_list_response struct {
	List          []*wPayments `json:"list"`
	Asset         string       `json:"asset"`
	Appid         string       `json:"appid"`
	FromPhone     string       `json:"from_phone"`
	FromPhoneCode string       `json:"from_phone_code"`
	ToPhone       string       `json:"to_phone"`
	ToPhoneCode   string       `json:"to_phone_code"`
	FromUser      string       `json:"from_user"`
	FromUserNo    string       `json:"from_user_no"`
	ToUser        string       `json:"to_user"`
	ToUserNo      string       `json:"to_user_no"`
	OrderId       string       `json:"order_id"`
	StartTime     int64        `json:"start_time"`
	EndTime       int64        `json:"end_time"`
	Status        string       `json:"status"`
	PageNumber    int64        `json:"page_number"`
	PageSize      int64        `json:"page_size"`
	Total         int64        `json:"total"`
	Retrieve      string       `json:"retrieve"`
	Seq           string       `json:"seq"`
	Result        int          `json:"result"`
	Comment       string       `json:"comment"`
}
```
### 1019.1 merchant_payment_list
//const  "**method**":"merchant_payment_list"
```
type merchant_payment_list_request struct { // fiters
	Asset       string `json:"asset"`
	Appid       string `json:"appid"`
	Phone       string `json:"phone"`
	PhoneCode   string `json:"phone_code"`
	UserNo      string `json:"user_no"`
	User        string `json:"user"`
	FromAddress string `json:"from_address"`
	StartTime   int64  `json:"start_time"`
	EndTime     int64  `json:"end_time"`
	Status      string `json:"status"`
	PageNumber  int64  `json:"page_number"`
	PageSize    int64  `json:"page_size"`
}

type iPayments struct {
	Id            string `json:"id"`
	Appid         string `json:"appid"`
	AssetName     string `json:"asset_name"`
	Amount        string `json:"amount"`
	Fee           string `json:"fee"`
	From          string `json:"from"`
	FromUser      string `json:"from_user"`
	FromPhone     string `json:"from_phone"`
	FromPhoneCode string `json:"from_phone_code"`
	FromUserNo    string `json:"from_user_no"`
	To            string `json:"to"`
	ToUser        string `json:"to_user"`
	ToPhone       string `json:"to_phone"`
	ToPhoneCode   string `json:"to_phone_code"`
	ToUserNo      string `json:"to_user_no"`
	OrderId       string `json:"order_id"`
	FeePaidBy     string `json:"fee_paid_by"`
	CallbackUrl   string `json:"callback_url"`
	RedirectUrl   string `json:"redirect_url"`
	CreateTime    string `json:"create_time"`
	UpdateTime    string `json:"update_time"`
	Status        string `json:"status"`
	PaidTotal     string `json:"paid_total"`
	FromBalance   string `json:"from_balance"`
	FromFrozen    string `json:"from_frozen"`
	ToBalance     string `json:"to_balance"`
	ToFrozen      string `json:"to_frozen"`
	AcceptedFrom  string `json:"accepted_from"`
	Merchantid    string `json:"merchantid"`
	MerchantName  string `json:"merchant_name"`
	FromAddress   string `json:"from_address"`
	ReturnRefid     string `json:"return_refid"`
}
type merchant_payment_list_response struct {
	List        []*iPayments `json:"list"`
	Asset       string       `json:"asset"`
	Appid       string       `json:"appid"`
	Phone       string       `json:"phone"`
	PhoneCode   string       `json:"phone_code"`
	UserNo      string       `json:"user_no"`
	FromAddress string       `json:"from_address"`
	StartTime   int64        `json:"start_time"`
	EndTime     int64        `json:"end_time"`
	Status      string       `json:"status"`
	PageNumber  int64        `json:"page_number"`
	PageSize    int64        `json:"page_size"`
	Total       int64        `json:"total"`
	Retrieve    string       `json:"retrieve"`
	Seq         string       `json:"seq"`
	Result      int          `json:"result"`
	Comment     string       `json:"comment"`
}
```
### 1020 redeem_list
//const  "**method**":"redeem_list"
```
type redeem_list_request struct { // fiters
	Appid      string `json:"appid"`
	Phone      string `json:"phone"`
	PhoneCode  string `json:"phone_code"`
	Status     string `json:"status"`
	StartTime  int64  `json:"start_time"`
	EndTime    int64  `json:"end_time"`
	PageNumber int64  `json:"page_number"`
	PageSize   int64  `json:"page_size"`
}

type iRedeems struct {
	Id              string `json:"id"`
	Appid           string `json:"appid"`
	User            string `json:"user"`
	Phone           string `json:"phone"`
	PhoneCode       string `json:"phone_code"`
	GzAmount        string `json:"gz_amount"`
	GoldAmount      string `json:"gold_amount"`
	GzAdminFee      string `json:"gz_admin_fee"`
	GzShippingFee   string `json:"gz_shipping_fee"`
	GzPaidTotal     string `json:"gz_paid_total"`
	DetailAddress   string `json:"detail_address"`
	DeliveryAddress string `json:"delivery_address"`
	TermsCondition  string `json:"terms_condition"`
	FrozenId        string `json:"frozen_id"`
	OrderId         string `json:"order_id"`
	CallbackUrl     string `json:"callback_url"`
	RedirectUrl     string `json:"redirect_url"`
	CreateTime      string `json:"create_time"`
	UpdateTime      string `json:"update_time"`
	Status          string `json:"status"`
	Fee             string `json:"fee"`
}
type redeem_list_response struct {
	List       []*iRedeems `json:"list"`
	Asset      string      `json:"asset"`
	Appid      string      `json:"appid"`
	Phone      string      `json:"phone"`
	PhoneCode  string      `json:"phone_code"`
	StartTime  int64       `json:"start_time"`
	EndTime    int64       `json:"end_time"`
	Status     string      `json:"status"`
	PageNumber int64       `json:"page_number"`
	PageSize   int64       `json:"page_size"`
	Total      int64       `json:"total"`
	Retrieve   string      `json:"retrieve"`
	Seq        string      `json:"seq"`
	Result     int         `json:"result"`
	Comment    string      `json:"comment"`
}
```
### 1021 withdraw_list
//const  "**method**":"withdraw_list"
//for superadmin&admin
```
type withdraw_list_request struct { // fiters
	Asset         string `json:"asset"`
	Appid         string `json:"appid"`
	FromPhone     string `json:"from_phone"`
	FromPhoneCode string `json:"from_phone_code"`
	FromUserNo    string `json:"from_user_no"`
	FromUser      string `json:"from_user"`
	ToAddress     string `json:"to_address"`
	StartTime     int64  `json:"start_time"`
	EndTime       int64  `json:"end_time"`
	Status        string `json:"status"`
	PageNumber    int64  `json:"page_number"`
	PageSize      int64  `json:"page_size"`
}

type iwithdraw_list_response struct {
	List          []*iWithdraws `json:"list"`
	Asset         string        `json:"asset"`
	Appid         string        `json:"appid"`
	FromPhone     string        `json:"from_phone"`
	FromPhoneCode string        `json:"from_phone_code"`
	FromUserNo    string        `json:"from_user_no"`
	FromUser      string        `json:"from_user"`
	ToAddress     string        `json:"to_address"`
	StartTime     int64         `json:"start_time"`
	EndTime       int64         `json:"end_time"`
	Status        string        `json:"status"`
	PageNumber    int64         `json:"page_number"`
	PageSize      int64         `json:"page_size"`
	Total         int64         `json:"total"`
	Retrieve      string        `json:"retrieve"`
	Seq           string        `json:"seq"`
	Result        int           `json:"result"`
	Comment       string        `json:"comment"`
}
```
### 1021 merchant_withdraw_list
//const  "**method**":"merchant_withdraw_list"
//the same with withdraw_list 
```
type merchant_withdraw_list_request struct { // fiters
	Asset      string `json:"asset"`
	Appid      string `json:"appid"`
	Phone      string `json:"phone"`
	PhoneCode  string `json:"phone_code"`
	To         string `json:"to"`
	UserNo     string `json:"user_no"`
	Orderid    string `json:"orderid"`
	StartTime  int64  `json:"start_time"`
	EndTime    int64  `json:"end_time"`
	Status     string `json:"status"`
	PageNumber int64  `json:"page_number"`
	PageSize   int64  `json:"page_size"`
}

type iWithdraws struct {
	Id            string `json:"id"`
	AssetName     string `json:"asset_name"`
	From          string `json:"from"`
	To            string `json:"to"`
	Amount        string `json:"amount"`
	CreateTime    string `json:"create_time"`
	UpdateTime    string `json:"update_time"`
	BlockNumber   string `json:"block_number"`
	TxHash        string `json:"tx_hash"`
	FromUser      string `json:"from_user"`
	ConfirmNumber uint64 `json:"confirm_number"`
	Vid           uint64 `json:"vid"`
	FromPhone     string `json:"from_phone"`
	FromPhoneCode string `json:"from_phone_code"`
	FromUserNo    string `json:"from_user_no"`
	ToPhone       string `json:"to_phone"`
	ToPhoneCode   string `json:"to_phone_code"`
	ToUserNo      string `json:"to_user_no"`
	Status        string `json:"status"`
	OriginId      string `json:"origin_id"`
	Appid         string `json:"appid"`
	Fee           string `json:"fee"`
	FeePaidBy     string `json:"fee_paid_by"`
	PaidTotal     string `json:"paid_total"`
	Orderid       string `json:"orderid"`
	GasFee        string `json:"gas_fee"`
	FromBalance   string `json:"from_balance"`
	FromFrozen    string `json:"from_frozen"`
	ToBalance     string `json:"to_balance"`
	ToFrozen      string `json:"to_frozen"`
	AcceptedFrom  string `json:"accepted_from"`
}

type merchant_withdraw_list_response struct {
	List       []*iWithdraws `json:"list"`
	Asset      string        `json:"asset"`
	Appid      string        `json:"appid"`
	Phone      string        `json:"phone"`
	PhoneCode  string        `json:"phone_code"`
	To         string        `json:"to"`
	UserNo     string        `json:"user_no"`
	Orderid    string        `json:"orderid"`
	StartTime  int64         `json:"start_time"`
	EndTime    int64         `json:"end_time"`
	Status     string        `json:"status"`
	PageNumber int64         `json:"page_number"`
	PageSize   int64         `json:"page_size"`
	Total      int64         `json:"total"`
	Retrieve   string        `json:"retrieve"`
	Seq        string        `json:"seq"`
	Result     int           `json:"result"`
	Comment    string        `json:"comment"`
}
```
### 1022 deposit_list
//const  "**method**":"deposit_list"
//for superadmin&admin
```
type deposit_list_request struct { // fiters
	Asset       string `json:"asset"`
	Appid       string `json:"appid"`
	ToPhone     string `json:"to_phone"`
	ToPhoneCode string `json:"to_phone_code"`
	ToUserNo    string `json:"to_user_no"`
	ToUser      string `json:"to_user"`
	StartTime   int64  `json:"start_time"`
	EndTime     int64  `json:"end_time"`
	Status      string `json:"status"`
	PageNumber  int64  `json:"page_number"`
	PageSize    int64  `json:"page_size"`
}

type iDeposits struct {
	Id            string `json:"id"`
	AssetName     string `json:"asset_name"`
	From          string `json:"from"`
	To            string `json:"to"`
	Amount        string `json:"amount"`
	CreateTime    string `json:"create_time"`
	UpdateTime    string `json:"update_time"`
	BlockNumber   string `json:"block_number"`
	TxHash        string `json:"tx_hash"`
	ToUser        string `json:"to_user"`
	ConfirmNumber uint64 `json:"confirm_number"`
	Vid           uint64 `json:"vid"`
	FromPhone     string `json:"from_phone"`
	FromPhoneCode string `json:"from_phone_code"`
	FromUserNo    string `json:"from_user_no"`
	ToPhone       string `json:"to_phone"`
	ToPhoneCode   string `json:"to_phone_code"`
	ToUserNo      string `json:"to_user_no"`
	Status        string `json:"status"`
	OriginId      string `json:"origin_id"`
	Appid         string `json:"appid"`
	FromBalance   string `json:"from_balance"`
	FromFrozen    string `json:"from_frozen"`
	ToBalance     string `json:"to_balance"`
	ToFrozen      string `json:"to_frozen"`
}
type ideposit_list_response struct {
	List        []*iDeposits `json:"list"`
	Asset       string       `json:"asset"`
	Appid       string       `json:"appid"`
	ToPhone     string       `json:"to_phone"`
	ToPhoneCode string       `json:"to_phone_code"`
	ToUserNo    string       `json:"to_user_no"`
	ToUser      string       `json:"to_user"`
	StartTime   int64        `json:"start_time"`
	EndTime     int64        `json:"end_time"`
	Status      string       `json:"status"`
	PageNumber  int64        `json:"page_number"`
	PageSize    int64        `json:"page_size"`
	Total       int64        `json:"total"`
	Retrieve    string       `json:"retrieve"`
	Seq         string       `json:"seq"`
	Result      int          `json:"result"`
	Comment     string       `json:"comment"`
}
```
### 1023 status config list
//const  "**method**":"status_config_list"

**Too See all status etc. here. just for dev**
```
https://vk4uikzpgc.execute-api.ap-east-1.amazonaws.com/dev/rpc
POST: {"method": "status_config_list"}
```
### 1024 get kyc file
//const  "**method**":"get_upload"
```
type get_upload_request struct {
	Fileid string `json:"fileid"`
}
type get_upload_response struct {
	Retrieve string `json:"retrieve"`
	Seq      string `json:"seq"`
	Body     string `json:"body"`
	Format   string `json:"format"`
}
```
### 1025 add_merchant
//const  "**method**":"add_merchant"
```

type add_merchant_req struct {
	Appid            string   `json:"appid"`
	User             string   `json:"user"`
	UserNo           string `json:"user_no"`
	Pubkey           string   `json:"pubkey"`
	UpdateTime       string   `json:"update_time"`
	UpdateUser       string   `json:"update_user"`
	Asset            string   `json:"asset"`
	Type             string   `json:"type"`
	Phone            string   `json:"phone"`
	PhoneCode        string   `json:"phone_code"`
	SmsRequire       string   `json:"sms_require"`
	AssetCallbackUrl string   `json:"asset_callback_url"`
	AuthRequire      string   `json:"auth_require"`
	CreateTime       string   `json:"create_time"`
	CreateUser       string   `json:"create_user"`
	IsInvestor       string   `json:"is_investor"`
	Status           string   `json:"status"`
	Parents          []string `json:"parents"`
	Children         []string `json:"children"`
	Universals       []string `json:"universals"`
	PaymentUrl       string `json:"payment_url"`
	FrozenUrl        string `json:"frozen_url"`
	AssetAddressUrl  string   `json:"asset_address_url"`
	QueryCallbackUrl string `json:"query_callback_url"`
	SmsTag           string   `json:"sms_tag"`
	ReportPsw        string `json:"report_psw"`
	BindUrl          string `json:"bind_url"`
	Md5key           string `json:"md5key"`
	SiteUrl          string   `json:"site_url"`
	Name             string   `json:"name"`
	ConfirmUrl       string   `json:"confirm_url"`
}

type add_merchant_resp struct {
	Appid            string   `json:"appid"`
	User             string   `json:"user"`
	UserNo           string `json:"user_no"`
	Pubkey           string   `json:"pubkey"`
	UpdateTime       string   `json:"update_time"`
	UpdateUser       string   `json:"update_user"`
	Asset            string   `json:"asset"`
	Type             string   `json:"type"`
	Phone            string   `json:"phone"`
	PhoneCode        string   `json:"phone_code"`
	SmsRequire       string   `json:"sms_require"`
	AssetCallbackUrl string   `json:"asset_callback_url"`
	AuthRequire      string   `json:"auth_require"`
	CreateTime       string   `json:"create_time"`
	CreateUser       string   `json:"create_user"`
	IsInvestor       string   `json:"is_investor"`
	Status           string   `json:"status"`
	Parents          []string `json:"parents"`
	Children         []string `json:"children"`
	Universals       []string `json:"universals"`
	PaymentUrl       string `json:"payment_url"`
	FrozenUrl        string `json:"frozen_url"`
	AssetAddressUrl  string   `json:"asset_address_url"`
	QueryCallbackUrl string `json:"query_callback_url"`
	SmsTag           string   `json:"sms_tag"`
	ReportPsw        string `json:"report_psw"`
	BindUrl          string `json:"bind_url"`
	Md5key           string `json:"md5key"`
	SiteUrl          string   `json:"site_url"`
	Name             string   `json:"name"`
	ConfirmUrl       string   `json:"confirm_url"`
	Retrieve         string   `json:"retrieve"`
	Seq              string   `json:"seq"`
	Result           int      `json:"result"`
	Comment          string   `json:"comment"`
}
```
### 1026 update_merchant
//const  "**method**":"update_merchant"
```

type update_merchant_req struct {
	Appid            string   `json:"appid"`
	User             string   `json:"user"`
	UserNo           string   `json:"user_no"`
	Pubkey           string   `json:"pubkey"`
	UpdateTime       string   `json:"update_time"`
	UpdateUser       string   `json:"update_user"`
	Asset            string   `json:"asset"`
	Type             string   `json:"type"`
	Phone            string   `json:"phone"`
	PhoneCode        string   `json:"phone_code"`
	SmsRequire       string   `json:"sms_require"`
	AssetCallbackUrl string   `json:"asset_callback_url"`
	AuthRequire      string   `json:"auth_require"`
	CreateTime       string   `json:"create_time"`
	CreateUser       string   `json:"create_user"`
	IsInvestor       string   `json:"is_investor"`
	Status           string   `json:"status"`
	Parents          []string `json:"parents"`
	Children         []string `json:"children"`
	Universals       []string `json:"universals"`
	PaymentUrl       string `json:"payment_url"`
	FrozenUrl        string `json:"frozen_url"`
	AssetAddressUrl  string   `json:"asset_address_url"`
	QueryCallbackUrl string `json:"query_callback_url"`
	SmsTag           string   `json:"sms_tag"`
	ReportPsw        string `json:"report_psw"`
	BindUrl          string `json:"bind_url"`
	Md5key           string `json:"md5key"`
	SiteUrl          string   `json:"site_url"`
	Name             string   `json:"name"`
	ConfirmUrl       string   `json:"confirm_url"`
}

type update_merchant_resp struct {
	Appid            string   `json:"appid"`
	User             string   `json:"user"`
	UserNo           string   `json:"user_no"`
	Pubkey           string   `json:"pubkey"`
	UpdateTime       string   `json:"update_time"`
	UpdateUser       string   `json:"update_user"`
	Asset            string   `json:"asset"`
	Type             string   `json:"type"`
	Phone            string   `json:"phone"`
	PhoneCode        string   `json:"phone_code"`
	SmsRequire       string   `json:"sms_require"`
	AssetCallbackUrl string   `json:"asset_callback_url"`
	AuthRequire      string   `json:"auth_require"`
	CreateTime       string   `json:"create_time"`
	CreateUser       string   `json:"create_user"`
	IsInvestor       string   `json:"is_investor"`
	Status           string   `json:"status"`
	Parents          []string `json:"parents"`
	Children         []string `json:"children"`
	Universals       []string `json:"universals"`
	PaymentUrl       string `json:"payment_url"`
	FrozenUrl        string `json:"frozen_url"`
	AssetAddressUrl  string   `json:"asset_address_url"`
	QueryCallbackUrl string `json:"query_callback_url"`
	SmsTag           string   `json:"sms_tag"`
	ReportPsw        string `json:"report_psw"`
	BindUrl          string `json:"bind_url"`
	Md5key           string `json:"md5key"`
	SiteUrl          string   `json:"site_url"`
	Name             string   `json:"name"`
	ConfirmUrl       string   `json:"confirm_url"`
	Retrieve         string   `json:"retrieve"`
	Seq              string   `json:"seq"`
	Result           int      `json:"result"`
	Comment          string   `json:"comment"`
}
```
### 1027 merchant_list
//const  "**method**":"merchant_list"
```

type merchant_list_req struct {
	Appid      string `json:"appid"`
	Phone      string `json:"phone"`
	PhoneCode  string `json:"phone_code"`
	StartTime  int64  `json:"start_time"`
	EndTime    int64  `json:"end_time"`
	Status     string `json:"status"`
	Parents    []string `json:"parents"`  //provide parent appid if superadmin
	Children   []string `json:"children"` //leave empty here
	PageNumber int64  `json:"page_number"`
	PageSize   int64  `json:"page_size"`
}
type iAppUsers struct {
	Appid            string   `json:"appid"`
	User             string   `json:"user"`
	UserNo           string   `json:"user_no"`
	Pubkey           string   `json:"pubkey"`
	UpdateTime       string   `json:"update_time"`
	UpdateUser       string   `json:"update_user"`
	Asset            string   `json:"asset"`
	Type             string   `json:"type"`
	Phone            string   `json:"phone"`
	PhoneCode        string   `json:"phone_code"`
	SmsRequire       string   `json:"sms_require"`
	AssetCallbackUrl string   `json:"asset_callback_url"`
	AuthRequire      string   `json:"auth_require"`
	CreateTime       string   `json:"create_time"`
	CreateUser       string   `json:"create_user"`
	IsInvestor       string   `json:"is_investor"`
	Status           string   `json:"status"`
	Parents          []string `json:"parents"`
	Children         []string `json:"children"`
	Universals       []string `json:"universals"`
	PaymentUrl       string `json:"payment_url"`
	FrozenUrl        string `json:"frozen_url"`
	AssetAddressUrl  string   `json:"asset_address_url"`
	QueryCallbackUrl string `json:"query_callback_url"`
	SmsTag           string   `json:"sms_tag"`
	ReportPsw        string `json:"report_psw"`
	BindUrl          string `json:"bind_url"`
	Md5key           string `json:"md5key"`
	SiteUrl          string   `json:"site_url"`
	Name             string   `json:"name"`
	ConfirmUrl       string   `json:"confirm_url"`
}
type merchant_list_resp struct {
	List       []*iAppUsers `json:"list"`
	Appid      string       `json:"appid"`
	Phone      string       `json:"phone"`
	PhoneCode  string       `json:"phone_code"`
	Status     string       `json:"status"`
	StartTime  int64        `json:"start_time"`
	EndTime    int64        `json:"end_time"`
	Total      int64        `json:"total"`
	PageNumber int64        `json:"page_number"`
	PageSize   int64        `json:"page_size"`
	Retrieve   string       `json:"retrieve"`
	Seq        string       `json:"seq"`
	Result     int          `json:"result"`
	Comment    string       `json:"comment"`
}

```
### 1028. do_redeem
//const  "**method**":"do_redeem"
```
type do_redeem_request struct {
	Id     string `json:"id"`
	Status string `json:"status"`
}

type do_redeem_response struct {
	Id       string `json:"id"`
	Status   string `json:"status"`
	Retrieve string `json:"retrieve"`
	Seq      string `json:"seq"`
	Result   int    `json:"result"`
	Comment  string `json:"comment"`
}
```
### 1029 mint_list
//const  "**method**":"mint_list"
```

type mint_list_request struct {
	Appid      string `json:"appid"`
	Id         string `json:"id"`
	TxHash     string `json:"tx_hash"`
	AssetName  string `json:"asset_name"`
	Phone      string `json:"phone"`
	PhoneCode  string `json:"phone_code"`
	StartTime  int64  `json:"start_time"`
	EndTime    int64  `json:"end_time"`
	Status     string `json:"status"`
	PageNumber int64  `json:"page_number"`
	PageSize   int64  `json:"page_size"`
}
type iMbts struct {
	Id            string `json:"id"`
	Appid         string `json:"appid"`
	User          string `json:"user"`
	Phone         string `json:"phone"`
	PhoneCode     string `json:"phone_code"`
	Type          string `json:"type"`
	Status        string `json:"status"`
	Operator      string `json:"operator"`
	Manager       string `json:"manager"`
	Comment       string `json:"comment"`
	CreateTime    string `json:"create_time"`
	UpdateTime    string `json:"update_time"`
	AssetName     string `json:"asset_name"`
	Amount        string `json:"amount"`
	Fee           string `json:"fee"`
	TxHash        string `json:"tx_hash"`
	From          string `json:"from"`
	To            string `json:"to"`
	BlockNumber   string `json:"block_number"`
	ConfirmNumber uint64 `json:"confirm_number"`
	Vid           uint64 `json:"vid"`
	OriginId      string `json:"origin_id"`
	PaidTotal     string `json:"paid_total"`
	FeePaidBy     string `json:"fee_paid_by"`
	OrderId       string `json:"order_id"`
}

type mint_list_response struct {
	List       []*iMbts `json:"list"`
	Appid      string   `json:"appid"`
	Id         string `json:"id"`
	TxHash     string `json:"tx_hash"`
	AssetName  string   `json:"asset_name"`
	Phone      string   `json:"phone"`
	PhoneCode  string   `json:"phone_code"`
	StartTime  int64    `json:"start_time"`
	EndTime    int64    `json:"end_time"`
	Status     string   `json:"status"`
	PageNumber int64    `json:"page_number"`
	PageSize   int64    `json:"page_size"`
	Total      int64    `json:"total"`
	Retrieve   string   `json:"retrieve"`
	Seq        string   `json:"seq"`
	Result     int      `json:"result"`
	Comment    string   `json:"comment"`
}

```
### 1030 burn_list
//const  "**method**":"burn_list"
```
type burn_list_request struct {
	Appid      string `json:"appid"`
	Id         string `json:"id"`
	TxHash     string `json:"tx_hash"`
	AssetName  string `json:"asset_name"`
	Phone      string `json:"phone"`
	PhoneCode  string `json:"phone_code"`
	StartTime  int64  `json:"start_time"`
	EndTime    int64  `json:"end_time"`
	Status     string `json:"status"`
	PageNumber int64  `json:"page_number"`
	PageSize   int64  `json:"page_size"`
}

type burn_list_response struct {
	List       []*iMbts `json:"list"`
	Appid      string   `json:"appid"`
	Id         string   `json:"id"`
	TxHash     string   `json:"tx_hash"`
	AssetName  string   `json:"asset_name"`
	Phone      string   `json:"phone"`
	PhoneCode  string   `json:"phone_code"`
	StartTime  int64    `json:"start_time"`
	EndTime    int64    `json:"end_time"`
	Status     string   `json:"status"`
	PageNumber int64    `json:"page_number"`
	PageSize   int64    `json:"page_size"`
	Total      int64    `json:"total"`
	Retrieve   string   `json:"retrieve"`
	Seq        string   `json:"seq"`
	Result     int      `json:"result"`
	Comment    string   `json:"comment"`
}

```
### 1031 is register
//const  "**method**":"isregister"
```
type retrieve_request struct {
	Appid     string      `json:"appid"`
	Sign      string      `json:"sign"`
	SignType  string      `json:"sign_type"`
	Name      string      `json:"name"`
	Phone     string      `json:"phone"`
	PhoneCode string      `json:"phone_code"`
	Token     string      `json:"token"`
	Retrieve   string   `json:"retrieve"`
	Seq        string   `json:"seq"`
	Data      interface{} `json:"data"`
}
type is_register_req struct {
	Appid     string `json:"appid"` // for superadmin, specify its parent appid
	Name      string `json:"name"`
	Phone     string `json:"phone"`
	PhoneCode string `json:"phone_code"`
	Email     string `json:"email"`
}

type is_register_resp struct {
	IsRegister string         `json:"is_registered"`
	Retrieve   string         `json:"retrieve"`
	Seq        string         `json:"seq"`
	Result     reterr.ErrCode `json:"result"`
	Comment    string         `json:"comment"`
}
```
### 1060.assets_config

used by admin,initially config

POST - https://vk4uikzpgc.execute-api.ap-east-1.amazonaws.com/dev/rpc

//const  "**method**":"assets_config"
```
type retrieve_request struct {
	Appid     string      `json:"appid"` // for example: GZWallet
	Sign      string      `json:"sign"`  // using signature alg mentioned next page
	SignType  string      `json:"sign_type"` // const "SHA256withRSA"
	Name      string      `json:"name"`
	Token     string      `json:"token"`
	Method    string      `json:"method"`
	Data      interface{} `json:"data"`
}

type assets_config_req struct {
	Name   string `json:"name"`
	Digits int32  `json:"digits"`
	Type   string `json:"type"`
	Index  string `json:"index"`
	Fee    string `json:"fee"`
	Appid  string `json:"appid"`
	Status string `json:"status"`
}

type assets_config_resp struct {
	Id       string `json:"id"`
	Name     string `json:"name"`
	Digits   int32  `json:"digits"`
	Type     string `json:"type"`
	Index    string `json:"index"`
	Fee      string `json:"fee"`
	Appid    string `json:"appid"`
	Status   string `json:"status"`
	Retrieve string `json:"retrieve"`
	Seq      string `json:"seq"`
	Result   int    `json:"result"`
	Comment  string `json:"comment"`
}

```
### 1061.symbol
used by admin,initially config

POST - https://vk4uikzpgc.execute-api.ap-east-1.amazonaws.com/dev/rpc

//const  "**method**":"symbol_config"
```
type retrieve_request struct {
	Appid     string      `json:"appid"` // for example: GZWallet
	Sign      string      `json:"sign"`  // using signature alg mentioned next page
	SignType  string      `json:"sign_type"` // const "SHA256withRSA"
	Name      string      `json:"name"`
	Token     string      `json:"token"`
	Method    string      `json:"method"`
	Data      interface{} `json:"data"`
}

type symbol_config_req struct {
	Token     string `json:"token"`
	User      string `json:"user"`
	Name      string `json:"name"`
	BaseCcy   string `json:"base_ccy"`
	ProfitCcy string `json:"profit_ccy"`
	LastPrice string `json:"last_price"`
	Appid     string `json:"appid"`
	Status    string `json:"status"`
	Bid       string `json:"bid"`
	Ask       string `json:"ask"`
}
type symbol_config_resp struct {
	Id        string `json:"id"`
	Name      string `json:"name"`
	BaseCcy   string `json:"base_ccy"`
	ProfitCcy string `json:"profit_ccy"`
	LastPrice string `json:"last_price"`
	Status    string `json:"status"`
	Bid       string `json:"bid"`
	Ask       string `json:"ask"`
	Retrieve  string `json:"retrieve"`
	Seq       string `json:"seq"`
	Appid     string `json:"appid"`
}
```

### 1062.chain_config

POST - https://vk4uikzpgc.execute-api.ap-east-1.amazonaws.com/dev/rpc

//const  "**method**":"chain_config"
used by admin,initially config

```
type retrieve_request struct {
	Appid     string      `json:"appid"` // for example: GZWallet
	Sign      string      `json:"sign"`  // using signature alg mentioned next page
	SignType  string      `json:"sign_type"` // const "SHA256withRSA"
	Name      string      `json:"name"`
	Token     string      `json:"token"`
	Method    string      `json:"method"`
	Data      interface{} `json:"data"`
}

type chain_config_req struct {
	AssetName    string `json:"asset_name"`
	InitNumber   string `json:"init_number"`
	UpdateNumber string `json:"update_number"`
}

type chain_config_resp struct {
	AssetName    string `json:"asset_name"`
	InitNumber   string `json:"init_number"`
	UpdateNumber string `json:"update_number"`
	Retrieve     string `json:"retrieve"`
	Seq          string `json:"seq"`
	Result       int    `json:"result"`
	Comment      string `json:"comment"`
}
```
### 1063 get kyc status
//const  "**method**":"kyc_status"
```
type retrieve_request struct {
	Appid     string      `json:"appid"` // for example: GZWallet
	Sign      string      `json:"sign"`  // using signature alg mentioned next page
	SignType  string      `json:"sign_type"` // const "SHA256withRSA"
	Name      string      `json:"name"`
	Token     string      `json:"token"`
	Method    string      `json:"method"`
	Data      interface{} `json:"data"`
}

type kyc_status_request struct {
	Appid     string `json:"appid"`
	Phone     string `json:"phone"`
	PhoneCode string `json:"phone_code"`
	Detail    string `json:"detail"` // empty for status only
}

type userKyc struct {
	Id                        string `json:"id"`
	Appid                     string `json:"appid"`
	UserNo                    string `json:"user_no"`
	User                      string `json:"user"`
	RandomNumber              string `json:"random_number"`
	PersonalType              string `json:"personal_type"`
	Portfolio                 string `json:"portfolio"`
	ResidentOf                string `json:"resident_of"`
	Title                     string `json:"title"`
	EnglishFullName           string `json:"english_full_name"`
	ChineseFullName           string `json:"chinese_full_name"`
	IdType                    string `json:"id_type"`
	IdNumber                  string `json:"id_number"`
	Birthday                  string `json:"birthday"`
	Nationality               string `json:"nationality"`
	ContactAddress            string `json:"contact_address"`
	City                      string `json:"city"`
	PostalCode                string `json:"postal_code"`
	CountryOfResidence        string `json:"country_of_residence"`
	Industry                  string `json:"industry"`
	Position                  string `json:"position"`
	YearsWithExistingEmployer string `json:"years_with_existing_employer"`
	AnnualIncome              string `json:"annual_income"`
	IncomeSource              string `json:"income_source"`
	NetAssetValue             string `json:"net_asset_value"`
	InvestAmount              string `json:"invest_amount"`
	InvestObjectives          string `json:"invest_objectives"`
	InvestHorizon             string `json:"invest_horizon"`
	InvestExperience          string `json:"invest_experience"`
	IdCardFront               string `json:"id_card_front"`
	IdCardBack                string `json:"id_card_back"`
	ProofOfAddress            string `json:"proof_of_address"`
	Selfie                    string `json:"selfie"`
	TermsConditions           string `json:"terms_conditions"`
	HowYouKnow                string `json:"how_you_know"`
	HowYouKnowOption          string `json:"how_you_know_option"`
	ReasonOpenAccount         string `json:"reason_open_account"`
	ReasonOpenAccountOption   string `json:"reason_open_account_option"`
	LaunderingViolation       string `json:"laundering_violation"`
	MoneyFromIllegal          string `json:"money_from_illegal"`
	HighRiskOfLaundering      string `json:"high_risk_of_laundering"`
	CreateTime                string `json:"create_time"`
	UpdateTime                string `json:"update_time"`
	Status                    string `json:"status"`
	Comment                   string `json:"comment"`
	InternalComment           string `json:"comment"`
}
type kyc_status_response struct {
	Kyc       *userKyc `json:"kyc",omitempty`
	Status    string   `json:"status"`
	Appid     string   `json:"appid"`
	Phone     string   `json:"phone"`
	PhoneCode string   `json:"phone_code"`
	Retrieve  string   `json:"retrieve"`
	Seq       string   `json:"seq"`
	Result    int      `json:"result"`
	Comment   string   `json:"comment"`
}
```
### 1064 get kyc list
//const  "**method**":"kyc_list"
```
type retrieve_request struct {
	Appid     string      `json:"appid"` // for example: GZWallet
	Sign      string      `json:"sign"`  // using signature alg mentioned next page
	SignType  string      `json:"sign_type"` // const "SHA256withRSA"
	Name      string      `json:"name"`
	Token     string      `json:"token"`
	Method    string      `json:"method"`
	Data      interface{} `json:"data"`
}

type kyc_list_request struct { // these are filters
	Appid      string `json:"appid"`
	Phone      string `json:"phone"`
	PhoneCode  string `json:"phone_code"`
	UserNo     string `json:"user_no"`
	StartTime  int64  `json:"start_time"`
	EndTime    int64  `json:"end_time"`
	Status     string `json:"status"`
	PageNumber int64  `json:"page_number"`
	PageSize   int64  `json:"page_size"`
}
type UserKycs struct {
	Id                        string   `json:"id"`
	Appid                     string   `json:"appid"`
	UserNo                    string   `json:"user_no"`
	User                      string   `json:"user"`
	Type                      string   `json:"type"`
	RandomNumber              string   `json:"random_number"`
	CreateTime                string   `json:"create_time"`
	UpdateTime                string   `json:"update_time"`
	Status                    string   `json:"status"`
	Operator                  string   `json:"operator"`
	Manager                   string   `json:"manager"`
	Comment                   string   `json:"comment"`
	PersonalType              string   `json:"personal_type"`
	Portfolio                 string   `json:"portfolio"`
	ResidentOf                string   `json:"resident_of"`
	Title                     string   `json:"title"`
	EnglishFullName           string   `json:"english_full_name"`
	ChineseFullName           string   `json:"chinese_full_name"`
	IdType                    string   `json:"id_type"`
	IdNumber                  string   `json:"id_number"`
	Birthday                  string   `json:"birthday"`
	Nationality               string   `json:"nationality"`
	ContactAddress            string   `json:"contact_address"`
	City                      string   `json:"city"`
	PostalCode                string   `json:"postal_code"`
	CountryOfResidence        string   `json:"country_of_residence"`
	Industry                  string   `json:"industry"`
	Position                  string   `json:"position"`
	YearsWithExistingEmployer string   `json:"years_with_existing_employer"`
	AnnualIncome              string   `json:"annual_income"`
	IncomeSource              string   `json:"income_source"`
	NetAssetValue             string   `json:"net_asset_value"`
	InvestAmount              string   `json:"invest_amount"`
	InvestObjectives          string   `json:"invest_objectives"`
	InvestHorizon             string   `json:"invest_horizon"`
	InvestExperience          string   `json:"invest_experience"`
	IdCardFront               string   `json:"id_card_front"`
	IdCardBack                string   `json:"id_card_back"`
	ProofOfAddress            string   `json:"proof_of_address"`
	Selfie                    string   `json:"selfie"`
	TermsConditions           string   `json:"terms_conditions"`
	HowYouKnow                string   `json:"how_you_know"`
	HowYouKnowOption          string   `json:"how_you_know_option"`
	ReasonOpenAccount         string   `json:"reason_open_account"`
	ReasonOpenAccountOption   string   `json:"reason_open_account_option"`
	LaunderingViolation       string   `json:"laundering_violation"`
	MoneyFromIllegal          string   `json:"money_from_illegal"`
	HighRiskOfLaundering      string   `json:"high_risk_of_laundering"`
	Appid                     string   `json:"appid"`
	Phone                     string   `json:"phone"`
	PhoneCode                 string   `json:"phone_code"`
}
type kyc_list_response struct {
	List []iproto.UserKycs		   `json:"list"`
	Appid        string            `json:"appid"`
	Phone        string            `json:"phone"`
	PhoneCode    string            `json:"phone_code"`
	StartTime    int64             `json:"start_time"`
	EndTime      int64             `json:"end_time"`
	Status       string            `json:"status"`
	PageNumber   int64             `json:"page_number"`
	PageSize     int64             `json:"page_size"`
	Total        int64             `json:"total"`
	Retrieve     string            `json:"retrieve"`
	Seq          string            `json:"seq"`
	Result       int               `json:"result"`
	Comment      string            `json:"comment"`
}
```
### 1065 do kyc 
//rpc
//const  "**method**":"do_kycs"
```
type retrieve_request struct {
	Appid     string      `json:"appid"` // for example: GZWallet
	Sign      string      `json:"sign"`  // using signature alg mentioned next page
	SignType  string      `json:"sign_type"` // const "SHA256withRSA"
	Name      string      `json:"name"`
	Token     string      `json:"token"`
	Method    string      `json:"method"`
	Data      interface{} `json:"data"`
}
type do_kyc_request struct { // for admin dev
	Id       string `json:"id"`
	User     string `json:"user"`
	Status   string `json:"status"`
	Operator string `json:"operator"`
	Manager  string `json:"manager"`
	Comment         string `json:"comment"`
	InternalComment string `json:"internal_comment"`
}

type do_kyc_response struct {
	Id       string `json:"id"`
	User     string `json:"user"`
	Status   string `json:"status"`
	Operator string `json:"operator"`
	Manager  string `json:"manager"`
	InternalComment string `json:"internal_comment"`
	Retrieve string `json:"retrieve"`
	Seq      string `json:"seq"`
	Result   int    `json:"result"`
	Comment  string `json:"comment"`
}
```
### 1066 mbt  list
//const  "**retrieve**":"mbt_list"
```
type mbt_list_request struct {
	Appid      string `json:"appid"`
	StartTime  int64  `json:"start_time"`
	EndTime    int64  `json:"end_time"`
	Status     string `json:"status"`
	PageNumber int64  `json:"page_number"`
	PageSize   int64  `json:"page_size"`
}

type mbt_list_response struct {
	MbtList    []iproto.Mbts `json:"mbt_list"`
	Appid      string        `json:"appid"`
	StartTime  int64         `json:"start_time"`
	EndTime    int64         `json:"end_time"`
	Status     string        `json:"status"`
	PageNumber int64         `json:"page_number"`
	PageSize   int64         `json:"page_size"`
	Total      int64         `json:"total"`
	Retrieve   string        `json:"retrieve"`
	Seq        string        `json:"seq"`
	Result     int           `json:"result"`
	Comment    string        `json:"comment"`
}
type Mbts struct {
	Id                   string   `json:"id"`
	Appid                string   `json:"appid"`
	User                 string   `json:"user"`
	Phone                string   `json:"phone"`
	PhoneCode            string   `json:"phone_code"`
	Type                 string   `json:"type"`
	Status               string   `json:"status"`
	Operator             string   `json:"operator"`
	Manager              string   `json:"manager"`
	Comment              string   `json:"comment"`
	CreateTime           string   `json:"create_time"`
	UpdateTime           string   `json:"update_time"`
	AssetName            string   `json:"asset_name"`
	Amount               string   `json:"amount"`
	Fee                  string   `json:"fee"`
	TxHash               string   `json:"tx_hash"`
	From                 string   `json:"from"`
	To                   string   `json:"to"`
	BlockNumber          string   `json:"block_number"`
	ConfirmNumber        uint64   `json:"confirm_number"`
	Vid                  uint64   `json:"vid"`
}
```

### 1069 do mbts
//const  "**method**":"do_mbts"
```
type retrieve_request struct {
	Appid     string      `json:"appid"` // for example: GZWallet
	Sign      string      `json:"sign"`  // using signature alg mentioned next page
	SignType  string      `json:"sign_type"` // const "SHA256withRSA"
	Name      string      `json:"name"`
	Token     string      `json:"token"`
	Method    string      `json:"method"`
	Data      interface{} `json:"data"`
}

type do_mbts_request struct {
	Mbts []*iproto.Mbts `json:"mbts"`
}
type do_mbts_response struct {
	FailedList []string `json:"failed_list"`
	Retrieve   string   `json:"retrieve"`
	Seq        string   `json:"seq"`
	Result     int      `json:"result"`
	Comment    string   `json:"comment"`
}
```
### 1070 fee config
//const  "**method**":"fee_config"
```
type retrieve_request struct {
	Appid     string      `json:"appid"` // for example: GZWallet
	Sign      string      `json:"sign"`  // using signature alg mentioned next page
	SignType  string      `json:"sign_type"` // const "SHA256withRSA"
	Name      string      `json:"name"`
	Token     string      `json:"token"`
	Method    string      `json:"method"`
	Data      interface{} `json:"data"`
}
type fee_config_req struct {
	Type string `json:type`
	Fee  string `json:"fee"`
}
type fee_config_resp struct {
	Retrieve   string   `json:"retrieve"`
	Seq        string   `json:"seq"`
	Result  int    `json:"result"`
	Comment string `json:"comment"`
}

```
### 1071 app user config, Use app_user_add,app_user_update instead.
～～//const  "**method**":"app_user_config"～～
```
type retrieve_request struct {
	Appid     string      `json:"appid"` // for example: GZWallet
	Sign      string      `json:"sign"`  // using signature alg mentioned next page
	SignType  string      `json:"sign_type"` // const "SHA256withRSA"
	Name      string      `json:"name"`
	Token     string      `json:"token"`
	Method    string   	  `json:"method"`
	Seq       string      `json:"seq"`
	Data      interface{} `json:"data"`
}

type app_user_config_req struct {
	User   string `json:"user"`
	Appid  string `json:"appid"`
	Pubkey string `json:"pubkey"`
	Asset  string `json:"asset"`
	Type   string `json:"type"`
}
type app_user_config_resp struct {
	User     string `json:"user"`
	Appid    string `json:"appid"`
	Pubkey   string `json:"pubkey"`
	Asset  string `json:"asset"`
	Type   string `json:"type"`
	Retrieve string `json:"retrieve"`
	Seq      string `json:"seq"`
	Result   int    `json:"result"`
	Comment  string `json:"comment"`
}
```
### 1072 asset addrs config
//const  "**method**":"asset_addrs_config"
```
type retrieve_request struct {
	Appid     string      `json:"appid"` // for example: GZWallet
	Sign      string      `json:"sign"`  // using signature alg mentioned next page
	SignType  string      `json:"sign_type"` // const "SHA256withRSA"
	Name      string      `json:"name"`
	Token     string      `json:"token"`
	Method    string   	  `json:"method"`
	Seq       string      `json:"seq"`
	Data      interface{} `json:"data"`
}

type asset_addrs_config_req struct {
	AssetType string   `json:"asset_type"`
	AddrList  []string `json:"address_list"`
	FromIndex int64    `json:"from_index"`
}

type asset_addrs_config_resp struct {
	AssetType string `json:"asset_type"`
	FromIndex int64  `json:"from_index"`
	Retrieve  string `json:"retrieve"`
	Seq       string `json:"seq"`
	Result    int    `json:"result"`
	Comment   string `json:"comment"`
}
```
### 1073 super admin create other systems's admin
//const  "**method**":"register_admins"
```
type register_req struct {
	Appid    string `json:"appid"`
	Name     string `json:"name"`
	Password string `json:"password"`
}

type register_resp struct {
	Name     string `json:"name"`
	Retrieve string `json:"retrieve"`
	Seq      string `json:"seq"`
	Result   int    `json:"result"`
	Comment  string `json:"comment"`
}
```
### 1074  assets_config_list
//const  "**method**":"assets_config_list"
```
type assets_config_list_request struct { // fiters
	Name string `json:"name"`
	//Digits int32  `json:"digits"`
	Type  string `json:"type"`
	Index string `json:"index"`
	Fee   string `json:"fee"`
	Appid string `json:"appid"`

	StartTime  int64  `json:"start_time"`
	EndTime    int64  `json:"end_time"`
	Status     string `json:"status"`
	PageNumber int64  `json:"page_number"`
	PageSize   int64  `json:"page_size"`
}

type assets_config_list_response struct {
	List []*iAssetConfigs `json:"list"`
	Name string           `json:"name"`
	//Digits int32            `json:"digits"`
	Type  string `json:"type"`
	Index string `json:"index"`
	Fee   string `json:"fee"`
	Appid string `json:"appid"`

	StartTime  int64  `json:"start_time"`
	EndTime    int64  `json:"end_time"`
	Status     string `json:"status"`
	PageNumber int64  `json:"page_number"`
	PageSize   int64  `json:"page_size"`
	Total      int64  `json:"total"`
	Retrieve   string `json:"retrieve"`
	Seq        string `json:"seq"`
	Result     int    `json:"result"`
	Comment    string `json:"comment"`
}

type iAssetConfigs struct {
	Name   string `json:"name"`
	Digits int32  `json:"digits"`
	Type   string `json:"type"`
	Index  string `json:"index"`
	Fee    string `json:"fee"`
	Appid  string `json:"appid"`
	Status string `json:"status"`
}
```
### 1075 asset_addrs_config_list
//const  "**method**":"asset_addrs_config_list"
```
type asset_addrs_config_list_request struct { // fiters
	AssetType string `json:"asset_type"`
	Index     int64  `json:"index"`
	Address   string `json:"address"`
	User      string `json:"user"`
	Appid     string `json:"appid"`
	UserXapp  string `json:"user_xapp"`

	StartTime  int64 `json:"start_time"`
	EndTime    int64 `json:"end_time"`
	PageNumber int64 `json:"page_number"`
	PageSize   int64 `json:"page_size"`
}

type asset_addrs_config_list_response struct {
	List      []*iAssetAddrsConfig `json:"list"`
	AssetType string               `json:"asset_type"`
	Index     int64                `json:"index"`
	Address   string               `json:"address"`
	User      string               `json:"user"`
	Appid     string               `json:"appid"`
	UserXapp  string               `json:"user_xapp"`

	StartTime  int64  `json:"start_time"`
	EndTime    int64  `json:"end_time"`
	PageNumber int64  `json:"page_number"`
	PageSize   int64  `json:"page_size"`
	Total      int64  `json:"total"`
	Retrieve   string `json:"retrieve"`
	Seq        string `json:"seq"`
	Result     int    `json:"result"`
	Comment    string `json:"comment"`
}

type iAssetAddrsConfig struct {
	AssetType  string `json:"asset_type"`
	Index      int64  `json:"index"`
	Address    string `json:"address"`
	CreateTime string `json:"create_time"`
	UpdateTime string `json:"update_time"`
	User       string `json:"user"`
	Appid      string `json:"appid"`
	UserXapp   string `json:"user_xapp"`
}
```
### 1076 symbol_config_list
//const  "**method**":"symbol_config_list"
```
type symbol_config_list_request struct { // fiters
	Name      string `json:"name"`
	BaseCcy   string `json:"base_ccy"`
	ProfitCcy string `json:"profit_ccy"`
	LastPrice string `json:"last_price"`
	Appid     string `json:"appid"`

	StartTime  int64  `json:"start_time"`
	EndTime    int64  `json:"end_time"`
	Status     string `json:"status"`
	PageNumber int64  `json:"page_number"`
	PageSize   int64  `json:"page_size"`
}

type symbol_config_list_response struct {
	List      []*iSymbolConfigs `json:"list"`
	Name      string            `json:"name"`
	BaseCcy   string            `json:"base_ccy"`
	ProfitCcy string            `json:"profit_ccy"`
	LastPrice string            `json:"last_price"`
	Appid     string            `json:"appid"`

	StartTime  int64  `json:"start_time"`
	EndTime    int64  `json:"end_time"`
	Status     string `json:"status"`
	PageNumber int64  `json:"page_number"`
	PageSize   int64  `json:"page_size"`
	Total      int64  `json:"total"`
	Retrieve   string `json:"retrieve"`
	Seq        string `json:"seq"`
	Result     int    `json:"result"`
	Comment    string `json:"comment"`
}

type iSymbolConfigs struct {
	Name      string `json:"name"`
	BaseCcy   string `json:"base_ccy"`
	ProfitCcy string `json:"profit_ccy"`
	LastPrice string `json:"last_price"`
	Appid     string `json:"appid"`
	Status    string `json:"status"`
	Bid       string `json:"bid"`
	Ask       string `json:"ask"`
}
```
### 1077 chain_config_list
//const  "**method**":"chain_config_list"
```
type chain_config_list_request struct { // fiters
	AssetName string `json:"asset_name"`

	StartTime  int64 `json:"start_time"`
	EndTime    int64 `json:"end_time"`
	PageNumber int64 `json:"page_number"`
	PageSize   int64 `json:"page_size"`
}

type chain_config_list_response struct {
	List      []*iChainConfig `json:"list"`
	AssetName string          `json:"asset_name"`

	StartTime  int64  `json:"start_time"`
	EndTime    int64  `json:"end_time"`
	PageNumber int64  `json:"page_number"`
	PageSize   int64  `json:"page_size"`
	Total      int64  `json:"total"`
	Retrieve   string `json:"retrieve"`
	Seq        string `json:"seq"`
	Result     int    `json:"result"`
	Comment    string `json:"comment"`
}

type iChainConfig struct {
	AssetName    string `json:"asset_name"`
	InitNumber   string `json:"init_number"`
	UpdateNumber string `json:"update_number"`
	UpdateTime   string `json:"update_time"`
	UpdateUser   string `json:"update_user"`
}
```
### 1078 asset_addr_index_config
//const  "**method**":"asset_addr_index_config"
```
type asset_addr_index_req struct {
	AssetName   string `json:"asset_name"`
	LatestIndex string `json:"latest_index"`
	Pubkey      string `json:"pubkey"`
}

type asset_addr_index_resp struct {
	AssetName   string `json:"asset_name"`
	LatestIndex string `json:"latest_index"`
	Retrieve    string `json:"retrieve"`
	Seq         string `json:"seq"`
	Result      int    `json:"result"`
	Comment     string `json:"comment"`
}
```
### 1079 asset_addr_index_config_list
//const  "**method**":"asset_addr_index_config_list"
```

type asset_addr_index_config_list_request struct { // fiters
	AssetName   string `json:"asset_name"`
	LatestIndex string `json:"latest_index"`
	Pubkey      string `json:"pubkey"`

	StartTime  int64 `json:"start_time"`
	EndTime    int64 `json:"end_time"`
	PageNumber int64 `json:"page_number"`
	PageSize   int64 `json:"page_size"`
}

type asset_addr_index_config_list_response struct {
	List        []*iAssetAddrIndexConfig `json:"list"`
	AssetName   string                   `json:"asset_name"`
	LatestIndex string                   `json:"latest_index"`
	Pubkey      string                   `json:"pubkey"`

	StartTime  int64  `json:"start_time"`
	EndTime    int64  `json:"end_time"`
	PageNumber int64  `json:"page_number"`
	PageSize   int64  `json:"page_size"`
	Total      int64  `json:"total"`
	Retrieve   string `json:"retrieve"`
	Seq        string `json:"seq"`
	Result     int    `json:"result"`
	Comment    string `json:"comment"`
}

type iAssetAddrIndexConfig struct {
	AssetName    string `json:"asset_name"`
	LatestIndex  string `json:"latest_index"`
	Pubkey       string `json:"pubkey"`
	Total        string `json:"total"`
	CreateTime   string `json:"create_time"`
	UpdateTime   string `json:"update_time"`
	LargestIndex int64  `json:"largest_index"`
}

```
### 1080 callback_error_list
//const  "**method**":"callback_error_list"
```
type callback_error_list_req struct {
	Appid       string `json:"appid"`
	User        string `json:"user"`
	Id          string `json:"id"`
	CallbackUrl string `json:"callback_url"`
	Msg         string `json:"msg"`
	Req         string `json:"req"`
	Status      string `json:"status"`
	Type        string `json:"type"`
	StartTime   int64  `json:"start_time"` //of create_time
	EndTime     int64  `json:"end_time"`

	PageNumber int64 `json:"page_number"`
	PageSize   int64 `json:"page_size"`
}
type iCallbackErrors struct {
	Appid       string `json:"appid"`
	User        string `json:"user"`
	Id          string `json:"id"`
	CallbackUrl string `json:"callback_url"`
	Msg         string `json:"msg"`
	Req         string `json:"req"`
	Status      string `json:"status"`
	Type        string `json:"type"`
	CreateTime  string `json:"create_time"`
	UpdateTime  string `json:"update_time"`
}
type callback_error_list_resp struct {
	List        []*iCallbackErrors `json:"list"`
	Appid       string             `json:"appid"`
	User        string             `json:"user"`
	Id          string             `json:"id"`
	CallbackUrl string             `json:"callback_url"`
	Msg         string             `json:"msg"`
	Req         string             `json:"req"`
	Status      string             `json:"status"`
	Type        string             `json:"type"`
	StartTime   int64              `json:"start_time"`
	EndTime     int64              `json:"end_time"`
	Total       int64              `json:"total"`
	PageNumber  int64              `json:"page_number"`
	PageSize    int64              `json:"page_size"`
	Retrieve    string             `json:"retrieve"`
	Seq         string             `json:"seq"`
	Result      int                `json:"result"`
	Comment     string             `json:"comment"`
}
```
### 1081 callback_error_retry
//const  "**method**":"callback_error_retry"
```
type callback_error_retry_req struct {
	User string `json:"user"`
	Id   string `json:"id"`
}

type callback_error_retry_resp struct {
	User     string `json:"user"`
	Id       string `json:"id"`
	Status   string `json:"status"`
	Retrieve string `json:"retrieve"`
	Seq      string `json:"seq"`
	Result   int    `json:"result"`
	Comment  string `json:"comment"`
}
```
### 1082 api_key_config
//super admin only
//const  "**method**":"api_key_config"
```
type apikey_req struct {
	Appid  string `json:"appid"`
	Token  string `json:"token"` // unique,if empty, will auto generate one
	User   string `json:"user"`
	Type   string `json:"type"`   // leave empty for feed
	Status string `json:"status"` // STATUS_NORMAL,STATUS_DELETED
}

type apikey_resp struct {
	Appid    string         `json:"appid"`
	Token    string         `json:"token"`
	User     string         `json:"user"`
	Type     string         `json:"type"`
	Status   string         `json:"status"`
	Retrieve string         `json:"retrieve"`
	Seq      string         `json:"seq"`
	Result   reterr.ErrCode `json:"result"`
	Comment  string         `json:"comment"`
}
```
### 1083 api_key_list
//super admin only
//const  "**method**":"api_key_list"
```
type api_key_list_req struct {
	Token      string `json:"token"`
	User       string `json:"user"`
	Type       string `json:"type"`   // leave empty for feed
	Status     string `json:"status"` // STATUS_NORMAL,STATUS_DELETED
	StartTime  int64  `json:"start_time"`
	EndTime    int64  `json:"end_time"`
	PageNumber int64  `json:"page_number"`
	PageSize   int64  `json:"page_size"`
}

type api_key_list_resp struct {
	List       []*iApiKey `json:"list"`
	Token      string     `json:"token"`
	User       string     `json:"user"`
	Type       string     `json:"type"`
	Status     string     `json:"status"`
	StartTime  int64      `json:"start_time"`
	EndTime    int64      `json:"end_time"`
	PageNumber int64      `json:"page_number"`
	PageSize   int64      `json:"page_size"`
	Total      int64      `json:"total"`
	Retrieve   string     `json:"retrieve"`
	Seq        string     `json:"seq"`
	Result     int        `json:"result"`
	Comment    string     `json:"comment"`
}
type iApiKey struct {
	Appid      string `json:"appid"`
	Token      string `json:"token"`
	User       string `json:"user"`
	Type       string `json:"type"`
	Status     string `json:"status"`
	CreateTime string `json:"create_time"`
}
```
### 1084 add_fee_config
//super admin only
//const  "**method**":"add_fee_config"
```

type add_fee_config_req struct {
	Appid      string `json:"appid"`
	AssetName  string `json:"asset_name"`
	Type       string `json:type`
	PerMillion string `json:"per_million"`
	PerTxFix   string `json:"per_tx_fix"`
	AuditMin   string `json:"audit_min"`
}
type add_fee_config_resp struct {
	Appid      string `json:"appid"`
	AssetName  string `json:"asset_name"`
	Type       string `json:type`
	PerMillion string `json:"per_million"`
	PerTxFix   string `json:"per_tx_fix"`
	AuditMin   string `json:"audit_min"`
	Retrieve   string `json:"retrieve"`
	Seq        string `json:"seq"`
	Result     int    `json:"result"`
	Comment    string `json:"comment"`
}
```
### 1085 update_fee_config
//super admin only
//const  "**method**":"update_fee_config"
```
type update_fee_config_req struct {
	Appid      string `json:"appid"`
	AssetName  string `json:"asset_name"`
	Type       string `json:type`
	PerMillion string `json:"per_million"`
	PerTxFix   string `json:"per_tx_fix"`
	AuditMin   string `json:"audit_min"`
	Status     string `json:"status"`
}
type update_fee_config_resp struct {
	Appid      string `json:"appid"`
	AssetName  string `json:"asset_name"`
	Type       string `json:type`
	PerMillion string `json:"per_million"`
	PerTxFix   string `json:"per_tx_fix"`
	AuditMin   string `json:"audit_min"`
	Status     string `json:"status"`
	Retrieve   string `json:"retrieve"`
	Seq        string `json:"seq"`
	Result     int    `json:"result"`
	Comment    string `json:"comment"`
}
```
### 1086 fee_config_list
//super admin only
//const  "**method**":"fee_config_list"
```
type fee_config_list_req struct {
	Appid      string `json:"appid"`
	AssetName  string `json:"asset_name"`
	Type       string `json:type`
	PerMillion string `json:"per_million"`
	PerTxFix   string `json:"per_tx_fix"`
	StartTime  int64  `json:"start_time"`
	EndTime    int64  `json:"end_time"`
	Status     string `json:"status"`
	PageNumber int64  `json:"page_number"`
	PageSize   int64  `json:"page_size"`
}

type iFeeConfig struct {
	Appid      string `json:"appid"`
	AssetName  string `json:"asset_name"`
	Type       string `json:type`
	PerMillion string `json:"per_million"`
	PerTxFix   string `json:"per_tx_fix"`
	AuditMin   string `json:"audit_min"`
	Status     string `json:"status"`
}
type fee_config_list_resp struct {
	List       []*iFeeConfig `json:"list"`
	Appid      string        `json:"appid"`
	AssetName  string        `json:"asset_name"`
	Type       string        `json:type`
	PerMillion string        `json:"per_million"`
	PerTxFix   string        `json:"per_tx_fix"`
	StartTime  int64         `json:"start_time"`
	EndTime    int64         `json:"end_time"`
	Status     string        `json:"status"`
	PageNumber int64         `json:"page_number"`
	PageSize   int64         `json:"page_size"`
	Total      int64         `json:"total"`
	Retrieve   string        `json:"retrieve"`
	Seq        string        `json:"seq"`
	Result     int           `json:"result"`
	Comment    string        `json:"comment"`
}
```
### 1087 merchant_transfer_approve
//const  "**method**":"merchant_transfer_approve"
```
type merchant_transfer_approve_req struct {
	Appid  string `json:"appid"`
	Id     string `json:"id"`
	Status string `json:"status"` //STATUS_REJECTED, default:STATUS_FINISHED
}
type merchant_transfer_approve_resp struct {
	Appid    string `json:"appid"`
	Id       string `json:"id"`
	Status   string `json:"status"`
	Retrieve string `json:"retrieve"`
	Seq      string `json:"seq"`
	Result   int    `json:"result"`
	Comment  string `json:"comment"`
}
```

### 1088 merchant_withdraw_approve
//const  "**method**":"merchant_withdraw_approve"
```
type merchant_withdraw_approve_req struct {
	Appid  string `json:"appid"`
	Id     string `json:"id"`
	Status string `json:"status"` //STATUS_REJECTED, default:STATUS_FINISHED
}
type merchant_withdraw_approve_resp struct {
	Appid    string `json:"appid"`
	Id       string `json:"id"`
	Status   string `json:"status"`
	Retrieve string `json:"retrieve"`
	Seq      string `json:"seq"`
	Result   int    `json:"result"`
	Comment  string `json:"comment"`
}
```
### 1089 add_menu/update_menu super&wallet&merchant
//const  "**method**":"add_menu"
//const  "**method**":"update_menu"
```
type add_menus_req struct {
	Appid    string `json:"appid"`
	RoleName string `json:"role_name"`
	MenuName string `json:"menu_name"`
	Parent  string `json:"parent"` //if empty, it's the first level; Level1MenuA/Level2MenuA1/Level3MenuA2
	Erights string `json:"erights"`
	Index   int32  `json:"index"`//sequence in the array 
	Type    string `json:"type"` //leave empty now
	Status  string `json:"status"`
}

type add_menus_resp struct {
	Appid    string `json:"appid"`
	RoleName string `json:"role_name"`
	MenuName string `json:"menu_name"`
	Parent   string `json:"parent"` //if empty, it's the first level
	Erights  string `json:"erights"`
	Index    int32  `json:"index"`
	Type     string `json:"type"`
	Status   string `json:"status"`
	Retrieve string `json:"retrieve"`
	Seq      string `json:"seq"`
	Result   int    `json:"result"`
	Comment  string `json:"comment"`
}
```
###1090 create_full_rights_role super&wallet&merchant
//const  "**method**":"create_full_rights_role"
```
type create_full_rights_role_req struct {
	Appid string `json:"appid"`
	Name  string `json:"name"`
}

type create_full_rights_role_resp struct {
	Appid    string `json:"appid"`
	Name     string `json:"name"`
	Retrieve string `json:"retrieve"`
	Seq      string `json:"seq"`
	Result   int    `json:"result"`
	Comment  string `json:"comment"`
}
```
### 1091 get_full_rights_role
//const  "**method**":"get_full_rights_role"
```
type get_full_rights_role_req struct {
	Appid string `json:"appid"`
	Name  string `json:"name"`
}

type get_full_rights_role_resp struct {
	Appid    string        `json:"appid"`
	Name     string        `json:"name"`
	Role     *iproto.Roles `json:"role"`
	Retrieve string        `json:"retrieve"`
	Seq      string        `json:"seq"`
	Result   int           `json:"result"`
	Comment  string        `json:"comment"`
}
```
### 1092 replace_role_menus
//const  "**method**":"replace_role_menus"
```
type Rrights struct {
	Type     string     `json:"type"`
	Erights  string     `json:"erights"`
	Parent   string     `json:"parent"`
	Status   string     `json:"status"`
	MenuName string     `json:"menu_name"`
	Rights   []*Rrights `json:"rights"`
}
type replace_role_menus_req struct {
	Appid  string          `json:"appid"`
	Name   string          `json:"name"`
	Power  string          `json:"power"`
	Rights *iproto.Rrights `json:"rights"`
	Status string          `json:"status"`
}

type replace_role_menus_resp struct {
	Appid    string          `json:"appid"`
	Name     string          `json:"name"`
	Power    string          `json:"power"`
	Rights   *iproto.Rrights `json:"rights"`
	Status   string          `json:"status"`
	Retrieve string          `json:"retrieve"`
	Seq      string          `json:"seq"`
	Result   int             `json:"result"`
	Comment  string          `json:"comment"`
}
```
### 1093 quotes
```
GET - https://vk4uikzpgc.execute-api.ap-east-1.amazonaws.com/dev/quotes?pairs=usdtcny&api_key=5c4baf36-c889-4713-bf30-5b4d433f69c9
GET - https://vk4uikzpgc.execute-api.ap-east-1.amazonaws.com/dev/quotes?pairs=USDTCNY&api_key=5c4baf36-c889-4713-bf30-5b4d433f69c9
pairs=symbolA,symbolB

```
### 1094 register no
//const  "**method**":"register_no"
```
type register_no_req struct {
	Appid     string `json:"appid"`
	NickName  string `json:"nick_name"`
	UserNo    string `json:"user_no"`
	Phone     string `json:"phone"`
	PhoneCode string `json:"phone_code"`
	Password  string `json:"password"`
	PinCode   string `json:"pin_code"`
}
type register_no_resp struct {
	Appid     string `json:"appid"`
	NickName  string `json:"nick_name"`
	UserNo    string `json:"user_no"`
	Phone     string `json:"phone"`
	PhoneCode string `json:"phone_code"`
	Retrieve  string `json:"retrieve"`
	Seq       string `json:"seq"`
	Result    int    `json:"result"`
	Comment   string `json:"comment"`
}
```
### 1095
//const  "**method**":"close_user"
```
type close_user_req struct {
	Appid     string `json:"appid"`
	PhoneCode string `json:"phone_code"`
	Phone     string `json:"phone"`
	/*
		Deleted    = 1;
		Closed     = 3;
		Frozen     = 4;
	*/
	Status int32 `json:"status"`
}
type close_user_resp struct {
	Appid     string `json:"appid"`
	PhoneCode string `json:"phone_code"`
	Phone     string `json:"phone"`
	Status    int32  `json:"status"`
	Retrieve  string `json:"retrieve"`
	Seq       string `json:"seq"`
	Result    int    `json:"result"`
	Comment   string `json:"comment"`
}
```
### 1096 
//const  "**method**":"update_user_lable"
```
type update_user_lable_req struct {
	Appid      string `json:"appid"`
	MerchantId string `json:"merchant_id"`
	PhoneCode  string `json:"phone_code"`
	Phone      string `json:"phone"`
	UserNo     string `json:"user_no"`
	Lable      string `json:"lable"`
}
type update_user_lable_resp struct {
	Appid      string `json:"appid"`
	MerchantId string `json:"merchant_id"`
	PhoneCode  string `json:"phone_code"`
	Phone      string `json:"phone"`
	UserNo     string `json:"user_no"`
	Lable      string `json:"lable"`
	Retrieve   string `json:"retrieve"`
	Seq        string `json:"seq"`
	Result     int    `json:"result"`
	Comment    string `json:"comment"`
}
```
### 1097 
//const  "**method**":"user_lable_list"
```
type user_lable_list_req struct {
	Appid      string `json:"appid"`
	MerchantId string `json:"merchant_id"`
	UserNo     string `json:"user_no"`
	Lable      string `json:"lable"`
	StartTime  int64  `json:"start_time"`
	EndTime    int64  `json:"end_time"`
	PageNumber int64  `json:"page_number"`
	PageSize   int64  `json:"page_size"`
}
type iUserLables struct {
	Appid          string `json:"appid"`
	MerchantidUser string `json:"merchantid_user"`
	Merchantid     string `json:"merchantid"`
	User           string `json:"user"`
	UserNo         string `json:"user_no"`
	Lable          string `json:"lable"`
	CreateTime     string `json:"create_time"`
}
type user_lable_list_resp struct {
	List       []*iUserLables `json:"list"`
	Appid      string         `json:"appid"`
	MerchantId string         `json:"merchant_id"`
	UserNo     string         `json:"user_no"`
	Lable      string         `json:"lable"`
	StartTime  int64          `json:"start_time"`
	EndTime    int64          `json:"end_time"`
	PageNumber int64          `json:"page_number"`
	PageSize   int64          `json:"page_size"`
	Total      int64          `json:"total"`
	Retrieve   string         `json:"retrieve"`
	Seq        string         `json:"seq"`
	Result     int            `json:"result"`
	Comment    string         `json:"comment"`
}
```
### 1098
//const  "**method**":"withdraw_approve"
```
type withdraw_approve_req struct {
	Appid  string `json:"appid"`
	Id     string `json:"id"`
	Status string `json:"status"` //STATUS_REJECTED, default:STATUS_FINISHED
}
type withdraw_approve_resp struct {
	Appid    string `json:"appid"`
	Id       string `json:"id"`
	Status   string `json:"status"`
	Retrieve string `json:"retrieve"`
	Seq      string `json:"seq"`
	Result   int    `json:"result"`
	Comment  string `json:"comment"`
}
```
### 1099
//const  "**method**":"user_lable"
```
type user_lable_req struct {
	Appid      string `json:"appid"`
	MerchantId string `json:"merchant_id"`
	UserNo     string `json:"user_no"`
}

type user_lable_resp struct {
	Appid      string `json:"appid"`
	MerchantId string `json:"merchant_id"`
	UserNo     string `json:"user_no"`
	Lable      string `json:"lable"`
	CreateTime string `json:"create_time"`
	Retrieve   string `json:"retrieve"`
	Seq        string `json:"seq"`
	Result     int    `json:"result"`
	Comment    string `json:"comment"`
}
```
### 1100
//const  "**method**":"frozen_list"
```
type frozen_list_request struct { // fiters
	Asset         string `json:"asset"`
	Appid         string `json:"appid"`
	FromPhone     string `json:"from_phone"`
	FromPhoneCode string `json:"from_phone_code"`
	FromUser      string `json:"from_user"`
	FromUserNo    string `json:"from_user_no"`
	StartTime     int64  `json:"start_time"`
	EndTime       int64  `json:"end_time"`
	Status        string `json:"status"`
	PageNumber    int64  `json:"page_number"`
	PageSize      int64  `json:"page_size"`
}

type frozen_list_response struct {
	List          []*iFrozens `json:"list"`
	Asset         string      `json:"asset"`
	Appid         string      `json:"appid"`
	FromPhone     string      `json:"from_phone"`
	FromPhoneCode string      `json:"from_phone_code"`
	FromUser      string      `json:"from_user"`
	FromUserNo    string      `json:"from_user_no"`
	StartTime     int64       `json:"start_time"`
	EndTime       int64       `json:"end_time"`
	Status        string      `json:"status"`
	PageNumber    int64       `json:"page_number"`
	PageSize      int64       `json:"page_size"`
	Total         int64       `json:"total"`
	Retrieve      string      `json:"retrieve"`
	Seq           string      `json:"seq"`
	Result        int         `json:"result"`
	Comment       string      `json:"comment"`
}

type iFrozens struct {
	Id              string `json:"id"`
	Appid           string `json:"appid"`
	AssetName       string `json:"asset_name"`
	Amount          string `json:"amount"`
	Fee             string `json:"fee"`
	From            string `json:"from"`
	FromUser        string `json:"from_user"`
	FromPhone       string `json:"from_phone"`
	FromPhoneCode   string `json:"from_phone_code"`
	To              string `json:"to"`
	ToUser          string `json:"to_user"`
	ToPhone         string `json:"to_phone"`
	ToPhoneCode     string `json:"to_phone_code"`
	OrderId         string `json:"order_id"`
	FeePaidBy       string `json:"fee_paid_by"`
	CreateTime      string `json:"create_time"`
	UpdateTime      string `json:"update_time"`
	Status          string `json:"status"`
	Reason          string `json:"reason"`
	RedeemId        string `json:"redeem_id"`
	InitAmount      string `json:"init_amount"`
	Merchantid      string `json:"merchantid"`
	Type            string `json:"type"`
	ToAppid         string `json:"to_appid"`
	FromUserNo      string `json:"from_user_no"`
	ToUserNo        string `json:"to_user_no"`
	FromFromBalance string `json:"from_from_balance"`
	FromFromFrozen  string `json:"from_from_frozen"`
	FromToBalance   string `json:"from_to_balance"`
	FromToFrozen    string `json:"from_to_frozen"`
	ToFromBalance   string `json:"to_from_balance"`
	ToFromFrozen    string `json:"to_from_frozen"`
	ToToBalance     string `json:"to_to_balance"`
	ToToFrozen      string `json:"to_to_frozen"`
	AcceptedFrom    string `json:"accepted_from"`
	PaidTotal       string `json:"paid_total"`
}
```
#1101
//const  "**method**":"frozen_xls"
```
type frozen_list_request struct { // fiters
	Asset         string `json:"asset"`
	Appid         string `json:"appid"`
	FromPhone     string `json:"from_phone"`
	FromPhoneCode string `json:"from_phone_code"`
	FromUser      string `json:"from_user"`
	FromUserNo    string `json:"from_user_no"`
	StartTime     int64  `json:"start_time"`
	EndTime       int64  `json:"end_time"`
	Status        string `json:"status"`
	PageNumber    int64  `json:"page_number"`
	PageSize      int64  `json:"page_size"`
}
type xls_response struct {
	Url      string `json:"url"`
	Retrieve string `json:"retrieve"`
	Seq      string `json:"seq"`
	Result   int    `json:"result"`
	Comment  string `json:"comment"`
}
```
#1102
//const  "**method**":"unfrozen_list"
```
type unfrozen_list_request struct { // fiters
	Asset         string `json:"asset"`
	Appid         string `json:"appid"`
	FromPhone     string `json:"from_phone"`
	FromPhoneCode string `json:"from_phone_code"`
	ToPhone       string `json:"to_phone"`
	ToPhoneCode   string `json:"to_phone_code"`
	FromUser      string `json:"from_user"`
	FromUserNo    string `json:"from_user_no"`
	ToUser        string `json:"to_user"`
	ToUserNo      string `json:"to_user_no"`
	StartTime     int64  `json:"start_time"`
	EndTime       int64  `json:"end_time"`
	Status        string `json:"status"`
	PageNumber    int64  `json:"page_number"`
	PageSize      int64  `json:"page_size"`
}

type unfrozen_list_response struct {
	List          []*iUnfrozens `json:"list"`
	Asset         string        `json:"asset"`
	Appid         string        `json:"appid"`
	FromPhone     string        `json:"from_phone"`
	FromPhoneCode string        `json:"from_phone_code"`
	ToPhone       string        `json:"to_phone"`
	ToPhoneCode   string        `json:"to_phone_code"`
	FromUser      string        `json:"from_user"`
	FromUserNo    string        `json:"from_user_no"`
	ToUser        string        `json:"to_user"`
	ToUserNo      string        `json:"to_user_no"`
	StartTime     int64         `json:"start_time"`
	EndTime       int64         `json:"end_time"`
	Status        string        `json:"status"`
	PageNumber    int64         `json:"page_number"`
	PageSize      int64         `json:"page_size"`
	Total         int64         `json:"total"`
	Retrieve      string        `json:"retrieve"`
	Seq           string        `json:"seq"`
	Result        int           `json:"result"`
	Comment       string        `json:"comment"`
}

type iUnfrozens struct {
	Id              string `json:"id"`
	Appid           string `json:"appid"`
	AssetName       string `json:"asset_name"`
	Amount          string `json:"amount"`
	Fee             string `json:"fee"`
	From            string `json:"from"`
	FromUser        string `json:"from_user"`
	FromPhone       string `json:"from_phone"`
	FromPhoneCode   string `json:"from_phone_code"`
	To              string `json:"to"`
	ToUser          string `json:"to_user"`
	ToPhone         string `json:"to_phone"`
	ToPhoneCode     string `json:"to_phone_code"`
	OrderId         string `json:"order_id"`
	FeePaidBy       string `json:"fee_paid_by"`
	CreateTime      string `json:"create_time"`
	UpdateTime      string `json:"update_time"`
	Status          string `json:"status"`
	Reason          string `json:"reason"`
	RedeemId        string `json:"redeem_id"`
	TakerOrderId    string `json:"taker_order_id"`
	Frozenid        string `json:"frozenid"`
	Merchantid      string `json:"merchantid"`
	Type            string `json:"type"`
	ToAppid         string `json:"to_appid"`
	FromUserNo      string `json:"from_user_no"`
	ToUserNo        string `json:"to_user_no"`
	FromFromBalance string `json:"from_from_balance"`
	FromFromFrozen  string `json:"from_from_frozen"`
	FromToBalance   string `json:"from_to_balance"`
	FromToFrozen    string `json:"from_to_frozen"`
	ToFromBalance   string `json:"to_from_balance"`
	ToFromFrozen    string `json:"to_from_frozen"`
	ToToBalance     string `json:"to_to_balance"`
	ToToFrozen      string `json:"to_to_frozen"`
	AcceptedFrom    string `json:"accepted_from"`
	PaidTotal       string `json:"paid_total"`
}
```
#1103
//const  "**method**":"unfrozen_xls"
```
type unfrozen_list_request struct { // fiters
	Asset         string `json:"asset"`
	Appid         string `json:"appid"`
	FromPhone     string `json:"from_phone"`
	FromPhoneCode string `json:"from_phone_code"`
	ToPhone       string `json:"to_phone"`
	ToPhoneCode   string `json:"to_phone_code"`
	FromUser      string `json:"from_user"`
	FromUserNo    string `json:"from_user_no"`
	ToUser        string `json:"to_user"`
	ToUserNo      string `json:"to_user_no"`
	StartTime     int64  `json:"start_time"`
	EndTime       int64  `json:"end_time"`
	Status        string `json:"status"`
	PageNumber    int64  `json:"page_number"`
	PageSize      int64  `json:"page_size"`
}
type xls_response struct {
	Url      string `json:"url"`
	Retrieve string `json:"retrieve"`
	Seq      string `json:"seq"`
	Result   int    `json:"result"`
	Comment  string `json:"comment"`
}
```
#1104
//const  "**method**":"tx_list"//for merchant usage
//const  "**method**":"user_tx_list"//for wallet usage, has to specify which user
//const  "**method**":"user_tx_xls"
// the response the same as 
```
type tx_list_request struct {
	Appid        string `json:"appid"`
	UserNo       string `json:"user_no"`
	User         string `json:"user"`
	Type         string `json:"type"`
	AcceptedFrom string `json:"accepted_from"` //APP, API, ADMIN, SUPER, SYSTEM
	Asset        string `json:"asset"`
	Address      string `json:"address"`
	StartTime    int64  `json:"start_time"`
	EndTime      int64  `json:"end_time"`
	PageNumber   int64  `json:"page_number"`
	PageSize     int64  `json:"page_size"`
}
type tx_in_one struct {
	Id            string `json:"id"`
	Asset         string `json:"asset"`
	Amount        string `json:"amount"`
	Fee           string `json:"fee"`
	FeePaidBy     string `json:"fee_paid_by"`
	PaidTotal     string `json:"paid_total"`
	OrderId       string `json:"order_id"`
	Status        string `json:"status"`
	Type          string `json:"type"` // TYPE_SEND,TYPE_RECV,TYPE_WITHDRAW,TYPE_DEPOSIT,TYPE_REDEEM,TYPE_PAYMENT,TYPE_RECV_PAYMENT,TYPE_UNFROZEN,TYPE_RECV_UNFROZEN
	FromPhone     string `json:"from_phone"`
	FromPhoneCode string `json:"from_phone_code"`
	FromUserNo    string `json:"from_user_no"`
	FromUser      string `json:"from_user"`
	FromAddr      string `json:"from_addr,omitempty"`
	ToPhone       string `json:"to_phone,omitempty"` //for payment privacy, not showing merchant's phone
	ToPhoneCode   string `json:"to_phone_code,omitempty"`
	ToUserNo      string `json:"to_user_no"`
	ToUser        string `json:"to_user"`
	ToAddr        string `json:"to_addr,omitempty"`
	CreateTime    string `json:"create_time"`
	Merchantid    string `json:"merchantid"`
	MerchantName  string `json:"merchant_name"`
	FromBalance   string `json:"from_balance"`
	FromFrozen    string `json:"from_frozen"`
	ToBalance     string `json:"to_balance"`
	ToFrozen      string `json:"to_frozen"`
	AcceptedFrom  string `json:"accepted_from"`
	GasFee        string `json:"gas_fee",omitempty`
}
type tx_list_response struct {
	TxList       []*tx_in_one `json:"tx_list"`
	Appid        string       `json:"appid"`
	UserNo       string       `json:"user_no"`
	User         string       `json:"user"`
	Type         string       `json:"type"`
	AcceptedFrom string       `json:"accepted_from"`
	Asset        string       `json:"asset"`
	Address      string       `json:"address"`
	StartTime    int64        `json:"start_time"`
	EndTime      int64        `json:"end_time"`
	PageNumber   int64        `json:"page_number"`
	PageSize     int64        `json:"page_size"`
	Total        int64        `json:"total"`
	Retrieve     string       `json:"retrieve"`
	Seq          string       `json:"seq"`
	Result       int          `json:"result"`
	Comment      string       `json:"comment"`
}
```
### 1105 digold kyc status
//const  "**method**":"digold_kyc_status"
```
type digold_kyc_status_request struct {
	Appid     string `json:"appid"`
	Phone     string `json:"phone"`
	PhoneCode string `json:"phone_code"`
	Detail    string `json:"detail"` // empty for status only
}

type digoldKyc struct {
	Id                       string `json:"id"`
	Appid                    string `json:"appid"`
	UserNo                   string `json:"user_no"`
	User                     string `json:"user"`
	RandomNumber             string `json:"random_number"`
	FullName                 string `json:"full_name"`
	Nationality              string `json:"nationality"`
	IdNumber                 string `json:"id_number"`
	IdType                   string `json:"id_type"`
	ContactAddress           string `json:"contact_address"`
	Telephone                string `json:"telephone"`
	Email                    string `json:"email"`
	Occupation               string `json:"occupation"`
	AnnualIncome             string `json:"annual_income"`
	SourceOfFund             string `json:"source_of_fund"`
	SourceOfFundOption       string `json:"source_of_fund_option"`
	ReasonOpenAccount        string `json:"reason_open_account"`
	HaveOtherWallet          string `json:"have_other_wallet"`
	HaveOtherWalletUSDAmount string `json:"have_other_wallet_usd_amount"`
	IdCardFront              string `json:"id_card_front"`
	IdCardBack               string `json:"id_card_back"`
	ProofOfAddress           string `json:"proof_of_address"`
	Selfie                   string `json:"selfie"`
	TermsConditions          string `json:"terms_conditions"`
}
type digold_kyc_status_response struct {
	Kyc       *digoldKyc `json:"kyc,omitempty"`
	Status    string     `json:"status"`
	Appid     string     `json:"appid"`
	Phone     string     `json:"phone"`
	PhoneCode string     `json:"phone_code"`
	Retrieve  string     `json:"retrieve"`
	Seq       string     `json:"seq"`
	Result    int        `json:"result"`
	Comment   string     `json:"comment"`
}
```
### 1106 get digold kyc list
//const  "**method**":"digold_kyc_list"
```
type kyc_proposal_list_request struct { // these are filters
	Appid      string `json:"appid"`
	Phone      string `json:"phone"`
	PhoneCode  string `json:"phone_code"`
	UserNo     string `json:"user_no"`
	StartTime  int64  `json:"start_time"`
	EndTime    int64  `json:"end_time"`
	Status     string `json:"status"`
	PageNumber int64  `json:"page_number"`
	PageSize   int64  `json:"page_size"`
}
type digold_kyc_proposal_list_response struct {
	List       []*digoldKyc `json:"list"`
	Appid      string       `json:"appid"`
	Phone      string       `json:"phone"`
	PhoneCode  string       `json:"phone_code"`
	StartTime  int64        `json:"start_time"`
	EndTime    int64        `json:"end_time"`
	Status     string       `json:"status"`
	UserNo     string       `json:"user_no"`
	PageNumber int64        `json:"page_number"`
	PageSize   int64        `json:"page_size"`
	Total      int64        `json:"total"`
	Retrieve   string       `json:"retrieve"`
	Seq        string       `json:"seq"`
	Result     int          `json:"result"`
	Comment    string       `json:"comment"`
}
```
### 1107 clear_google_code (superadmin only)
//const  "**method**":"clear_google_code"
```
type clear_google_code_req struct {
	Appid string `json:"appid"`
	Name  string `json:"name"`
}
type clear_google_code_resp struct {
	Retrieve string `json:"retrieve"`
	Seq      string `json:"seq"`
	Result   int    `json:"result"`
	Comment  string `json:"comment"`
}
```
### 1108 update user password
//const  "**method**":"update_password" 
```
type update_password_req struct {
	OldPassword string `json:"old_password"`
	NewPassword string `json:"new_password"`
}

type update_password_resp struct {
	Retrieve string         `json:"retrieve"`
	Seq      string         `json:"seq"`
	Result   reterr.ErrCode `json:"result"`
	Comment  string         `json:"comment"`
}
```
### 1109 bind_google_code //use to bind again or clear binding,need token here
//const  "**method**":"bind_google_code" 
```
type bind_google_code_req struct {
	Secret     string `json:"secret"` //if secret is empty, will clear the binding
	GoogleCode string `json:"google_code"`
}
type bind_google_code_resp struct {
	Retrieve string `json:"retrieve"`
	Seq      string `json:"seq"`
	Result   int    `json:"result"`
	Comment  string `json:"comment"`
}
```
### 1110 merchant_withdraw DELETED
//const  "**method**":"merchant_withdraw" 
```
type merchant_withdraw_request struct {
	OrderId      string `json:"order_id"`
	AssetName    string `json:"asset_name"`
	Amount       string `json:"amount"`
	To           string `json:"to"` //withdraw to address
	MerchantName string `json:"merchant_name"`
	Comment      string `json:"comment"`
}

type merchant_withdraw_response struct {
	Retrieve          string `json:"retrieve"`
	Seq               string `json:"seq"`
	OrderId           string `json:"order_id"`
	Id                string `json:"id"`
	AssetName         string `json:"asset_name"`
	Amount            string `json:"amount"`
	To                string `json:"to"`
	Fee               string `json:"fee"`
	CreateTime        string `json:"create_time"`
	IsTransfer        bool   `json:"is_transfer"`
	MerchantName      string `json:"merchant_name"`
	PaymentId         string `json:"payment_id,omitempty"`
	PaymentMerchantid string `json:"payment_merchantid,omitempty"`
	PaymentToUserNo   string `json:"payment_to_user_no,omitempty"`
	Status            string `json:"status"`
	Result            int    `json:"result"`
	Comment           string `json:"comment"`
}
```
### 1110 merchant_submit_settlement DELETED
//const  "**method**":"merchant_submit_settlement" 
```
type upload_request struct {
	AssetName   string `json:"asset_name"`
	Body        string `json:"body"`
	TotalAmount string `json:"total_amount"`
	TotalNumber int64  `json:"total_number"`
}
//body file format:
to,amount(x10^6),asset_name
0x4e0f3A3Ba617Eec25b422Da9428E736A7f9261A7,10000000000000,USDT
0x4e0f3A3Ba617Eec25b422Da9428E736A7f9261A7,12200000000000,USDT

type upload_response struct {
	FileId      string `json:"fileid"`
	FailedIndex int64  `json:"failed_index"` //[1:total_number]
	Retrieve    string `json:"retrieve"`
	Seq         string `json:"seq"`
	Result      int    `json:"result"`
	Comment     string `json:"comment"`
}
```
### 1111 merchant_user_info
//const  "**method**":"merchant_user_info" 
```
type merchant_user_info_req struct {
}
type merchant_user_info struct {
	AssetName string `json:"asset_name"`
	Address   string `json:"address"`
	Balance   string `json:"balance"`
	Frozen    string `json:"frozen"`
	UpdateTime string `json:"update_time"`
}
type merchant_user_info_resp struct {
	UserNo   string                `json:"user_no"`
	Assets   []*merchant_user_info `json:"assets"`
	Retrieve string                `json:"retrieve"`
	Seq      string                `json:"seq"`
	Result   reterr.ErrCode        `json:"result"`
	Comment  string                `json:"comment"`
}
```
### 1112 merchant_submit_single_settlement
//const  "**method**":"merchant_submit_single_settlement" 
```
type merchant_submit_single_settlement_request struct {
	Amount  string `json:"amount"`
	To      string `json:"to"` //withdraw to address
	Comment string `json:"comment"`
}

type merchant_submit_single_settlement_response struct {
	Retrieve  string `json:"retrieve"`
	Seq       string `json:"seq"`
	Id        string `json:"id"`
	AssetName string `json:"asset_name"`
	Amount    string `json:"amount"`
	To        string `json:"to"`
	Status    string `json:"status"`
	Result    int    `json:"result"`
	Comment   string `json:"comment"`
}
```
### 1113 merchant_submit_batch_settlement
//const  "**method**":"merchant_submit_batch_settlement" 
```
type merchant_submit_batch_settlement_request struct {
	AssetName   string `json:"asset_name"`
	Body        string `json:"body"`
	TotalAmount string `json:"total_amount"`
	TotalNumber int64  `json:"total_number"`
}

type merchant_submit_batch_settlement_response struct {
	BatchId  string `json:"batch_id"`
	Retrieve string `json:"retrieve"`
	Seq      string `json:"seq"`
	Result   int    `json:"result"`
	Comment  string `json:"comment"`
}
```
### 1114 merchant_settlement_list
//const  "**method**":"merchant_settlement_list" 
```

type merchant_settlement_list_request struct { // fiters
	Asset              string `json:"asset"`
	Appid              string `json:"appid"`
	Phone              string `json:"phone"`
	PhoneCode          string `json:"phone_code"`
	To                 string `json:"to"`
	UserNo             string `json:"user_no"`
	User               string `json:"user"`
	Orderid            string `json:"orderid"`
	StartTime          int64  `json:"start_time"`
	EndTime            int64  `json:"end_time"`
	Status             string `json:"status"`
	PageNumber         int64  `json:"page_number"`
	PageSize           int64  `json:"page_size"`
	CreatedBy          string `json:"created_by"`//审批人
	UpdatedBy          string `json:"updated_by"`//审批人
	UpdatedByStartTime int64  `json:"updated_by_start_time"`//审批更新时间
	UpdatedByEndTime   int64  `json:"updated_by_end_time"`//审批更新时间
}

type iWithdraws struct {
	Id            string `json:"id"`
	AssetName     string `json:"asset_name"`
	From          string `json:"from"`
	To            string `json:"to"`
	Amount        string `json:"amount"`
	CreateTime    string `json:"create_time"`
	UpdateTime    string `json:"update_time"`
	BlockNumber   string `json:"block_number"`
	TxHash        string `json:"tx_hash"`
	FromUser      string `json:"from_user"`
	ConfirmNumber uint64 `json:"confirm_number"`
	Vid           uint64 `json:"vid"`
	FromPhone     string `json:"from_phone"`
	FromPhoneCode string `json:"from_phone_code"`
	FromUserNo    string `json:"from_user_no"`
	ToPhone       string `json:"to_phone"`
	ToPhoneCode   string `json:"to_phone_code"`
	ToUserNo      string `json:"to_user_no"`
	Status        string `json:"status"`
	OriginId      string `json:"origin_id"`
	Appid         string `json:"appid"`
	Fee           string `json:"fee"`
	FeePaidBy     string `json:"fee_paid_by"`
	PaidTotal     string `json:"paid_total"`
	Orderid       string `json:"orderid"`
	GasFee        string `json:"gas_fee"`
	FromBalance   string `json:"from_balance"`
	FromFrozen    string `json:"from_frozen"`
	ToBalance     string `json:"to_balance"`
	ToFrozen      string `json:"to_frozen"`
	AcceptedFrom  string `json:"accepted_from"`
	Merchantid    string `json:"merchantid"`
	MerchantName  string `json:"merchant_name"`
	CreatedBy     string `json:"created_by"`
	UpdatedBy     string `json:"updated_by"`
	Comment       string `json:"comment"`
	BatchId       string `json:"batch_id"`
	UpdatedByTime string `json:"updated_by_time"`//审批更新时间
	Reason        string `json:"reason"`
}
type merchant_settlement_list_response struct {
	List       []*iWithdraws `json:"list"`
	Asset      string        `json:"asset"`
	Appid      string        `json:"appid"`
	Phone      string        `json:"phone"`
	PhoneCode  string        `json:"phone_code"`
	To         string        `json:"to"`
	UserNo     string        `json:"user_no"`
	Orderid    string        `json:"orderid"`
	StartTime  int64         `json:"start_time"`
	EndTime    int64         `json:"end_time"`
	Status     string        `json:"status"`
	PageNumber int64         `json:"page_number"`
	PageSize   int64         `json:"page_size"`
	Total      int64         `json:"total"`
	Retrieve   string        `json:"retrieve"`
	Seq        string        `json:"seq"`
	Result     int           `json:"result"`
	Comment    string        `json:"comment"`
}
```
### 1115 merchant_settlement_approve
//const  "**method**":"merchant_settlement_approve" 
```
type merchant_settlement_approve_req struct {
	Appid  string `json:"appid"`
	Id     string `json:"id"`
	Status string `json:"status"` //STATUS_REJECTED, default:STATUS_FINISHED
}
type merchant_settlement_approve_resp struct {
	Appid             string `json:"appid"`
	Id                string `json:"id"`
	AssetName         string `json:"asset_name"`
	Amount            string `json:"amount"`
	To                string `json:"to"`
	Fee               string `json:"fee"`
	CreateTime        string `json:"create_time"`
	IsTransfer        bool   `json:"is_transfer"`
	PaymentId         string `json:"payment_id,omitempty"`
	PaymentMerchantid string `json:"payment_merchantid,omitempty"`
	PaymentToUserNo   string `json:"payment_to_user_no,omitempty"`
	Status            string `json:"status"`
	Retrieve          string `json:"retrieve"`
	Seq               string `json:"seq"`
	Result            int    `json:"result"`
	Comment           string `json:"comment"`
}
```
### 1116 return_transfer
//const  "**method**":"return_transfer" 
```
type return_transfer_req struct {
	Id       string `json:"id"`
	Appid    string `json:"appid"`
	Password string `json:"password"`
	Status   string `json:"status"` //STATUS_REJECTED, STATUS_RETURN_PENDING, STATUS_FINISHED
}
type return_transfer_resp struct {
	Id       string `json:"id"`
	ReturnId string `json:"return_id"`
	Retrieve string `json:"retrieve"`
	Seq      string `json:"seq"`
	Status   string `json:"status"`
	Result   int    `json:"result"`
	Comment  string `json:"comment"`
}
```
### 1117 return_payment
//const  "**method**":"return_payment" 
```
type return_payment_req struct {
	Id       string `json:"id"`
	Appid    string `json:"appid"`
	Password string `json:"password"`
	Status   string `json:"status"` //STATUS_REJECTED, STATUS_RETURN_PENDING, STATUS_FINISHED
}
type return_payment_resp struct {
	Id       string `json:"id"`
	ReturnId string `json:"return_id"`
	Retrieve string `json:"retrieve"`
	Seq      string `json:"seq"`
	Status   string `json:"status"`
	Result   int    `json:"result"`
	Comment  string `json:"comment"`
}
```
### 1118 role_name_list
//const  "**method**":"role_name_list" 
```
type role_name_list_req struct {
	Appid string `json:"appid"`
}

type role_name_list_resp struct {
	Appid     string   `json:"appid"`
	RoleNames []string `json:"role_names"`
	Retrieve  string   `json:"retrieve"`
	Seq       string   `json:"seq"`
	Result    int      `json:"result"`
	Comment   string   `json:"comment"`
}
```
### 1119 address_query
//const  "**method**":"address_query"
```
type address_query_req struct {
	Address string `json:"address"`
}
type address_query_resp struct {
	Address      string         `json:"address"`
	Phone        string         `json:"phone"`
	PhoneCode    string         `json:"phone_code"`
	UserNo       string         `json:"user_no"`
	Status       string         `json:"status"`      //STATUS_NOT_FOUND,STATUS_OCCUPIED
	MerchantId   string         `json:"merchant_id"` //if merchant id is not empty, it is subasset
	MerchantName string         `json:"merchant_name"`
	Logoid       string         `json:"logoid"`
	Type         string         `json:"type"` //TYPE_WALLET_ASSET,TYPE_MERCHANT_SUBASSET
	Retrieve     string         `json:"retrieve"`
	Seq          string         `json:"seq"`
	Result       reterr.ErrCode `json:"result"`
	Comment      string         `json:"comment"`
}
```
### 1120 assets_gen
//const  "**method**":"assets_gen"
```
type assets_gen_req struct {
	Appid        string `json:"appid"`
	PhoneCode    string `json:"phone_code"`
	Phone        string `json:"phone"`
	UserNo       string `json:"user_no"`
	AssetName    string `json:"asset_name"`
	Merchantid   string `json:"merchant_id"`
	MerchantName string `json:"merchant_name"`
}

type assets_gen_resp struct {
	Appid     string `json:"appid"`
	PhoneCode string `json:"phone_code"`
	Phone     string `json:"phone"`
	UserNo    string `json:"user_no"`
	AssetName string `json:"asset_name"`
	Address   string `json:"address"`
	Retrieve  string `json:"retrieve"`
	Seq       string `json:"seq"`
	Result    int    `json:"result"`
	Comment   string `json:"comment"`
}
```
### 1121 merchant_callback_list
//const  "**method**":"merchant_callback_list"
```
type merchant_callback_list_req struct {
	User        string `json:"user"`
	Id          string `json:"id"` //provide this: id, orderid,txhash
	Address     string `json:"address"`//this could be from or to address
	UserNo      string `json:"user_no"`//this could be from or to userno
	CallbackUrl string `json:"callback_url"`
	Status      string `json:"status"`
	Type        string `json:"type"`
	StartTime   int64  `json:"start_time"` //of create_time
	EndTime     int64  `json:"end_time"`

	PageNumber int64 `json:"page_number"`
	PageSize   int64 `json:"page_size"`
}
type iCallbackErrors struct {
	Appid       string `json:"appid"`
	User        string `json:"user"`
	Id          string `json:"id"`
	CallbackUrl string `json:"callback_url"`
	Msg         string `json:"msg"`
	Req         string `json:"req"`
	Refid       string `json:"refid"`
	OrderId     string `json:"order_id"`
	TxHash      string `json:"tx_hash"`
	Merchantid  string `json:"merchantid"`
	FromUserNo  string `json:"from_user_no"`
	ToUserNo    string `json:"to_user_no"`
	FromAddr    string `json:"from_address"`
	ToAddr      string `json:"to_address"`
	AssetName   string `json:"asset_name"`
	Amount      string `json:"amount"`
	Fee         string `json:"fee"`
	Status      string `json:"status"`
	Type        string `json:"type"`
	CreateTime  string `json:"create_time"`
	UpdateTime  string `json:"update_time"`
}
type merchant_callback_list_resp struct {
	List        []*iCallbackErrors `json:"list"`
	User        string             `json:"user"`
	Id          string             `json:"id"`
	CallbackUrl string             `json:"callback_url"`
	Status      string             `json:"status"`
	Type        string             `json:"type"`
	StartTime   int64              `json:"start_time"` //of create_time
	EndTime     int64              `json:"end_time"`

	PageNumber int64  `json:"page_number"`
	PageSize   int64  `json:"page_size"`
	Total      int64  `json:"total"`
	Retrieve   string `json:"retrieve"`
	Seq        string `json:"seq"`
	Result     int    `json:"result"`
	Comment    string `json:"comment"`
}
```
### 1122 merchant_callback_retry
//const  "**method**":"merchant_callback_retry"
```
type merchant_callback_retry_req struct {
	User string `json:"user"`
	Id   string `json:"id"`
}
type merchant_callback_retry_resp struct {
	User     string `json:"user"`
	Id       string `json:"id"`
	Retrieve string `json:"retrieve"`
	Seq      string `json:"seq"`
	Result   int    `json:"result"`
	Comment  string `json:"comment"`
}
```
# Deploy
1. When deploy individually, the total size would increase according to the numbers of function.

2. When change index of dynamodb, has to change the name of resources.

3. When migrates dynamodb, backup&copy data.

# Config
1. AssetAddrIndex
2. AssetConfig
3. ChainConfig
4. SymbolConfig
5. AppidUserConfig
6. AddFeedUserSubscribe
7. feed_url,ws_domain,pubkey,appid,time_out
# ClientType
enum et{
		TYPE_INITIAL = 0;
		TYPE_PC  = 1;
		TYPE_WEB = 2;
		TYPE_IOS = 3;
		TYPE_ANDROID = 4;
		TYPE_ADMIN   = 5;
		TYPE_FEED    = 6;
		TYPE_OAUTH   = 7;
		TYPE_ADMIN_SCAN = 8;
		TYPE_IPAD    = 9 ;
		TYPE_MACOS   = 10;
		TYPE_OTC     = 11;
		TYPE_READONLY = 12;
		TYPE_SUPER_ADMIN = 13;
		TYPE_WALLET_ADMIN = 14;
		TYPE_MERCHANT_ADMIN = 15;
		TYPE_MERCHANT_REPORT = 16;
		TYPE_MERCHANT_CENTER = 17;
 } 
eg. "TYPE_ANDROID"
# Return Code
	0 : OK : success
	1 : FAIL : failure
	2 : USER_NOT_FOUND : user not found
	3 : PASSWORD_INCORRECT : password incorrect
	4 : AWS_ERROR : aws error
	5 : NO_LOGIN : login require
	6 : EXPIRED : session expired
	7 : TOKEN_INVALID : token invalid
	8 : PINCODE_INVALID : pincode invalid
	9 : AMOUNT_INVALID : amount invalid
	10 : FRIEND_ALREADY_ADDED : friend already added
	11 : SEND_SMS_TOO_FREQUENT : send sms too frequent
	12 : NO_THIS_METHOD : no this method
	13 : SYMBOL_NOT_EXIST : symbol not exist
	14 : TX_ERROR : transact failed
	15 : NO_THIS_TICKET : no this ticket
	16 : CANCEL_FAIL : cannot cancel
	17 : SYSTEM_ERROR : system error
	18 : ARGS_INVALID : args invalid
	19 : OVER_MAX_LENGTH : over max length
	20 : ALREADY_EXISTS : already exists
	21 : ROLE_NOT_FOUND : role not found
	22 : ORDER_NOT_FOUND : order not found
	23 : ASSET_NOT_FOUND : asset not found
	24 : NO_RIGHTS : no rights
	25 : NO_ROLES : no roles
	26 : NOT_BOOL : should be YES or NO
	27 : NOT_STATUS : invalid status value
	28 : FROZEN_NOT_FOUND : frozen not found
	29 : FROZEN_DONE_ALREADY : frozen done already
	30 : NOT_TYPE : type invalid
	31 : KYC_NOT_FOUND : kyc not found
	32 : RN_REQUIRED : random number required
	33 : KYC_DONE_ALREADY : kyc done already
	34 : APPID_NOT_FOUND : merchant not found
	35 : MERCHANT_NOT_FOUND : unknown wallet
	36 : REDEEM_NOT_FOUND : redeem not found
	37 : WITHDRAW_NOT_FOUND : withdraw not found
	38 : MBT_NOT_FOUND : mint or burn not found
	39 : REDEEM_DONE_ALREADY : redeem done already
	40 : SIGN_INVALID : sign invalid
	41 : ETH_ADDRESS_INVALID : eth address invalid
	42 : BTC_ADDRESS_INVALID : btc address invalid
	43 : ALREADY_REGISTERED : already registered
	44 : MERCHANT_INVALID : merchant invalid
	45 : ASSET_INVALID : asset invalid
	46 : BALANCE_NOT_ENOUGH : balance not enough
	47 : ADDRESS_ALREADY_EXISTS : address already exist
	48 : ADDRESS_NOT_ENOUGH : no address
	49 : ADDRESS_INDEX_INVALID : address index invalid
	50 : PUBKEY_INVALID : pubkey invalid
	51 : ADDRESS_ALREADY_IN_USE : address already in use
	52 : PRICE_NOT_VALID : price not valid
	53 : BANK_ACCONT_NOT_FOUND : bank account not found
	54 : BANK_ACCONT_INVALID : bank account invalid
	55 : OVER_MAX_TOTAL : over max total
	56 : BANK_ACCONT_NOT_AVAILABLE : bank account not available
	57 : ORDER_TICKET_NOT_SUBMITED : ticket not submited
	58 : ORDER_CANCELED : order canceled
	59 : ORDER_EXPIRED : order expired
	60 : ORDER_ALREADY_DONE : order already done
	61 : ORDER_REJECTED : order rejected
	62 : SEND_SMS_FAILED : send sms failed
	63 : FEE_NOT_FOUND : fee not found
	64 : FEE_CALC_FAILED : fee calc failed
	65 : TYPE_INVALID : type invalid
	66 : REQUEST_TOO_FREQUENT : request too frequent
	67 : SMS_REQUIRED : sms required
	68 : NOT_SUPPORT : not supported yet
	69 : BIND_ALREADY : bind already
	70 : BIND_ANOTHER_ALREADY : phone bind another user already
	71 : TRY_AGAIN_LATER : try again later
	72 : DEPOSIT_NOT_FOUND : deposit not found
	73 : USER_NOT_IN_CHANNEL : user not in channel
	74 : CHANNEL_NOT_FOUND : channel not found
	75 : DEVICE_NOT_FOUND : user device not found
	76 : MSG_NOT_FOUND : msg not found
	77 : NO_FROZEN : frozen not found
	78 : FROZEN_INVALID : frozen invalid
	79 : TIME_INVALID : time invalid
	80 : MENU_NOT_FOUND : menu not found
	81 : USER_INVALID : user invalid
	82 : TOKEN_KICK_OUT : token kick out
	83 : MENU_DUPLICATED : menu duplicated
	84 : VERSION_NOT_FOUND : version not found
	85 : NEED_RESET_PASSWORD : need reset password
	86 : AWS_S3_ERROR : aws s3 error
	87 : ENCRYPT_ERROR : encrypt error
	88 : ORDER_CLOSED : order closed
	89 : PINCODE_TOO_FREQUENT : pin code locked
	90 : APPID_INVALID : appid invalid
	91 : ADDRESS_NOT_FOUND : address not found
	92 : NOT_ENABLED : not enabled
	93 : TWOFA_INVALD : twofa code invalid
	94 : USER_FORCE_OUT : user deleted
	95 : NEED_RESET_TWOFA : need reset twofa
# Sign
### key generation:
openssl genrsa -out private.pem 2048
openssl rsa -in private.pem -outform PEM -pubout -out public.pem
openssl pkcs8 -topk8 -inform PEM -in private.pem -outform PEM -nocrypt > private_pkcs8.pem
**the alg below is under modification**
**https://github.com/kjur/jsrsasign/tree/master/sample**
```
<script language="JavaScript" type="text/javascript" src="../jsrsasign-all-min.js"></script>
<script language="JavaScript" type="text/javascript" src="../ext/cj/enc-base64.js"></script>

function sign(privateKey, str){
 var sig = new KJUR.crypto.Signature({"alg": "SHA256withRSA"});
 sig.init(privateKey);
 var sortdata = oprint(JSON.parse(str),true);
 sig.updateString(sortdata);
 var hSigVal = sig.sign();
 return hextob64(hSigVal);
}
function parseobj(v, ini) {
  // console.log(v, "not array");
  var vv;
  var ir = [];
  for (var j in v) {
      if (j == "sign") continue;
      if (typeof v[j] === 'object') {
        //   console.log(v, j, "is object");
          if (ini) {
              ir.push(j + "=" + oprint(v[j], false));
          } else {
              ir.push(j + ":" + oprint(v[j], false));
          }
      } else {
        //   console.log(v, j, "not object");
          if (ini) {
              ir.push(j + "=" + v[j]);
          } else {
              ir.push(j + ":" + v[j]);
          }
      }
  }
  ir.sort();
  if (ini) {
      vv = ir.join("&");
  } else {
      vv = "map[" + ir.join(" ") + "]";
  }
  return vv;
}
function parsearr(v) {
  var ir = [];
  for (var i in v) {
      if (typeof v[i] === 'object') {
          ir.push(oprint(v[i], false));
      } else if (v[i] instanceof Array) {
          ir.push(parsearr(v[i]));
      } else {
          ir.push(v[i]);
      }
  }
  var vv = "[" + ir.join(" ") + "]";
  return vv;
}
function oprint(v, ini) {
  var vv;
  if (typeof v === 'object') {
      if (v instanceof Array) {
          vv = parsearr(v);
      } else {
          vv = parseobj(v, ini)
      }
  } else {
      vv = v
  }
  // console.log(vv);
  return vv;
}
```
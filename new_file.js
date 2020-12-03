<script language="JavaScript" type="text/javascript" src="../jsrsasign-all-min.js"></script>


function sign(privateKey, str){
 var sig = new KJUR.crypto.Signature({"alg": "SHA256withRSA"});
 sig.init(privateKey);
 var sortdata = oprint(JSON.parse(str),true);
 sig.updateString(sortdata);
 var hSigVal = sig.sign();
 return hextob64(hSigVal);
}

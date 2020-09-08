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

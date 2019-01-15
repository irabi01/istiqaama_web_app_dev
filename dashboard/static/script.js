var chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXTZabcdefghiklmnopqrstuvwxyz";
var string_length = 6;
var randomstring = '';
for (var i=0; i<string_length; i++) {
  var rnum = Math.floor(Math.random() * chars.length);
  randomstring += chars.substring(rnum,rnum+1);
}
// document.randform.randomfield.value = randomstring;
document.getElementById('id_member_id').value = randomstring;

function checkboxHandler(self){
  var id = self.getAttribute('id');
  var chk = document.getElementById(id);
    if (chk.checked) {
         chk.parentNode.style.textDecoration = 'line-through';
         chk.parentNode.style.textDecorationColor = 'pink';
         chk.style.display="none";
    } else {
         chk.parentNode.style.textDecoration = 'none';
         chk.style.display="inline";
    }
}
// 아무리 해도 안 되길래 htmlinputelement가 계속 떠서 한번 더 들어가야 체크박스내에 영향이 있을 것 같았다. 근데 더 올라가야 하네? 이건 이유를 잘 모르겠다. 이렇게 간단한 코드...였다니...

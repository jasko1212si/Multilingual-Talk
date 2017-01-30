var xhttp = new XMLHttpRequest();
xhttp.open("GET", "/request-messages", true);
xhttp.send();

xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      var scrolledToBottom = ($(window).scrollTop() + $(window).height() == $(document).height());
      document.getElementById("messages").innerHTML = xhttp.responseText;
      if(scrolledToBottom){
        window.scrollTo(0,document.body.scrollHeight);
      }
    }
};

var interval = setInterval(function () {
  xhttp.open("GET", "/request-messages", true);
  xhttp.send();
}, 3000);


function getCaret(el) {
    if (el.selectionStart) {
        return el.selectionStart;
    } else if (document.selection) {
        el.focus();
        var r = document.selection.createRange();
        if (r == null) {
            return 0;
        }
        var re = el.createTextRange(), rc = re.duplicate();
        re.moveToBookmark(r.getBookmark());
        rc.setEndPoint('EndToStart', re);
        return rc.text.length;
    }
    return 0;
}

$('textarea').keyup(function (event) {
    if (event.keyCode == 13) {
        var content = this.value;
        var caret = getCaret(this);
        if(event.shiftKey){
            this.value = content.substring(0, caret - 1) + "\n" + content.substring(caret, content.length);
            event.stopPropagation();
        } else {
            this.value = content.substring(0, caret - 1) + content.substring(caret, content.length);
            $('form').submit();
        }
    }
});

window.scrollTo(0,document.body.scrollHeight);

function ContactPost() {
    const form = document.getElementById('contactpost');
    const eventName = form.querySelector("[name='eventName']");
    const endDate = form.querySelector("[name='endDate']");
    const comment = form.querySelector("[name='comment']");
    const possibleDate = form.querySelector("[name=possibleDate]");

    // 未入力がなければ確認メッセージを出して送信、未入力がある場合は未入力メッセージ表示
    if (eventName.value && comment.value && endDate.value && possibleDate) { 
        const confirmMessage = (`作成します。よろしいですか`);
        if (window.confirm(confirmMessage)) {
        form.submit();
        }
    }
        else {
            window.alert('未入力項目があります。');
        }
    }


// function sendmaker(){
//     window.location.href = '/make_event.html'
// }
$(document).ready(function () {
    make_table();
 });
 // 表作成
 function make_table() {
    let t = '';
    t += '<thead>';
    t += '<tr>';
    ['イベントリンク','イベント名','期限','作成者','作成日'].forEach(function (v) {
        t += '<th class="color_head">' + v + '</th>';
    });
    t += '</tr>';
    t += '</thead>';
    $('#content').html(t);
 }
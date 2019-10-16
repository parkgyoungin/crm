var checked = function(id){
    return document.getElementById(id).checked == true;
}
var nonChecked = function(id){
    return document.getElementById(id).checked == false;
}
var selected_etc = function(id){
    return document.getElementById(id).value == '직접입력(추가)';
}
var selected_another = function(id){
    return document.getElementById(id).value != '직접입력(추가)';
}
var selected_ex_none = function(id){
    return (document.getElementById(id).value != '') && (document.getElementById(id).value != '직접입력(추가)');
}
var able = function(id){
    document.getElementById(id).removeAttribute('disabled');
}
var disable = function(id){
    document.getElementById(id).setAttribute('disabled', 'true');
}
var set_checked = function(id){
    document.getElementById(id).checked = true;
}
function set_another_js(ele, connections, sets){
    function get_row(id){
        for(var i=0; i<connections.length; i++){
            var j = connections[i].findIndex((item) => {
                return item == id;
            });
            if(j>-1)
                return [i,j];
        }
    }

    function set(row, main, sub){
        col = row[1];
        if(col == main[0]){
            if(main[1]( connections[row[0]][row[1]] )){
                for(var i=0; i<sub.length; i++){
                    sub[i][1]( connections[row[0]][sub[i][0]] );
                }
            }
        }
    }

    var row = get_row(ele.id);
    if(row){
        for(var i=0; i<sets.length; i++){
            set(row,sets[i]['main'], sets[i]['sub']);
        }
    }
}

function search(model, field_name){
    var url_mask = "/post/search/" + model + '/' + field_name;
    child = window.open(url_mask, 'window팝업', 'width=400, height=400, menubar=no, status=no, toolbar=no');
}

function btn_get_url_js(key, ele, request){
    var val = get_btn_value(ele);
    result = "?";
    for(var r in request){
        if (r != key)
            result += get_sentence(r, request[r]) ;
    }
    result += get_sentence(key, val);
    return result;
}

function get_url_js(key, val, request){
    result = "?";
    for(var r in request){
        if (r != key)
            result += get_sentence(r, request[r]) ;
    }
    result += get_sentence(key, val);
    return result;
}

function get_sentence(key, val){
    result = "&" + key + "=" + val;
    return result;
}

function get_btn_value(ele){
    var inner = ele.innerHTML;
    var last = inner.substr(inner.length - 1);
    if(last == '▼')
        return ele.id;
    else
        return '-' + ele.id;
}

function search_address_js(ids) {
    new daum.Postcode({
        oncomplete: function(data) {
            // 팝업에서 검색결과 항목을 클릭했을때 실행할 코드를 작성하는 부분.

            // 도로명 주소의 노출 규칙에 따라 주소를 표시한다.
            // 내려오는 변수가 값이 없는 경우엔 공백('')값을 가지므로, 이를 참고하여 분기 한다.
            var roadAddr = data.roadAddress; // 도로명 주소 변수
            var extraRoadAddr = ''; // 참고 항목 변수

            // 법정동명이 있을 경우 추가한다. (법정리는 제외)
            // 법정동의 경우 마지막 문자가 "동/로/가"로 끝난다.
            if(data.bname !== '' && /[동|로|가]$/g.test(data.bname)){
                extraRoadAddr += data.bname;
            }
            // 건물명이 있고, 공동주택일 경우 추가한다.
            if(data.buildingName !== '' && data.apartment === 'Y'){
               extraRoadAddr += (extraRoadAddr !== '' ? ', ' + data.buildingName : data.buildingName);
            }
            // 표시할 참고항목이 있을 경우, 괄호까지 추가한 최종 문자열을 만든다.
            if(extraRoadAddr !== ''){
                extraRoadAddr = ' (' + extraRoadAddr + ')';
            }

            // 우편번호와 주소 정보를 해당 필드에 넣는다.
            document.getElementById(ids['zip']).value = data.zonecode;
            document.getElementById(ids['add']).value = roadAddr;
            document.getElementById(ids['add_old']).value = data.jibunAddress;

            // 참고항목 문자열이 있을 경우 해당 필드에 넣는다.
            if(roadAddr !== ''){
                document.getElementById(ids['note']).value = extraRoadAddr;
            } else {
                document.getElementById(ids['note']).value = '';
            }


        }
    }).open();
}

function popup_check(model, field_name, id){
    var model_field = '/' + model + '/' + field_name + '/' + id;
    var url_mask = "/post/check/abc/def/ghi".replace('/abc/def/ghi', model_field);
    child = window.open(url_mask, 'window팝업', 'width=400, height=400, menubar=no, status=no, toolbar=no');
}

function set_reverse(){
    reverse = document.getElementById('reverse').value;
    if(reverse == 'true')
        document.getElementById('reverse').value = 'false';
    else
        document.getElementById('reverse').value = 'true';
    form.submit();
}

function check_login(user_id){
    if(user_id)
}
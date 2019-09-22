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

function get_url_js(key, ele, request){
    var val = get_btn_value(ele);
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

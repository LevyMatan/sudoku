
addEventListener('input', (event) => updateValue(event));
addEventListener('click', (event) => onclick(event));
addEventListener('mousedown', (event) => onmousedown(event));
addEventListener('mouseup', (event) => onmouseup(event));

var red_cell = -1;
var hignlighted_cell;
function checkValidCellInput(input) {
    var regex=/[1-9]/;
    if (input == input.match(regex))
    {
        return true;
    }
    return false;
}
function checkElementsInRow(cell_idx, cell_value) {
    let row = Math.floor(cell_idx / 9);
    for (let index = 0; index < 9; index++) {
        const cell_id = (row * 9) + index;
        if (cell_id == cell_idx) {
            continue;
        }
        const cell = document.getElementById('cell-' + cell_id);
        if(cell.value == cell_value){
            setRedCell(cell_id);
            return cell_id;
        }
        
    }
    return -1;
}
function checkElementsInCol(cell_idx, cell_value) {
    let col = cell_idx % 9;
    // document.getElementById("log").innerHTML = col
    for (let index = 0; index < 9; index++) {
        const cell_id = (index * 9) + col;
        if (cell_id == cell_idx) {
            continue;
        }
        const cell = document.getElementById('cell-' + cell_id);
        if(cell.value == cell_value){
            setRedCell(cell_id);
            return cell_id;
        }
        
    }
    return -1;
}


function checkElementsInBox(cell_idx, cell_value) {
    let col = cell_idx % 9;
    let row = Math.floor(cell_idx / 9);
    let start_col = col - (col%3);
    let start_row = row - (row%3);
    for (let row_idx = start_row; row_idx < start_row+3; row_idx++) {
        for (let col_idx = start_col; col_idx < start_col+3; col_idx++) {

            let cell_id = row_idx*9 + col_idx;
            if (cell_id == cell_idx) {
                continue;
            }
            const cell = document.getElementById('cell-' + cell_id);
            if(cell.value == cell_value){
                setRedCell(cell_id);
                return cell_id;
            }
        }
    }
    return -1;
}


function updateValue(e) {
    // document.getElementById('values').innerHTML = "Hello from event!";
    clearRedCell();
    let input_value = e.target.value;
    let cell_idx = e.target.id.match(/[0-9]+/);
    if (checkValidCellInput(input_value) == false)
    {
        setRedCell(cell_idx);
        e.target.value = '';
    }
    else
    {
        document.getElementById('values3').innerHTML = "Cell of ID: " + cell_idx;
        let row = checkElementsInRow(cell_idx, input_value);
        if(row > 0){
            e.target.value = '';
            return;
        }
        
        let col = checkElementsInCol(cell_idx, input_value);
        if(col > 0){
            e.target.value = '';
            return;
        }
        let box = checkElementsInBox(cell_idx, input_value);
        if(box > 0){
            e.target.value = '';
            return;
        }
    }
}

function setRedCell(idx) {
    document.getElementById('cell-' + idx).style.backgroundColor = 'red';
    red_cell = idx;
}

function clearRedCell() {
    if (red_cell != -1) {
        
        const cell = document.getElementById("cell-" + red_cell)
        if (cell.disabled == true) {
            cell.style.backgroundColor = 'rgb(238, 238, 238)';
        }
        else {
            cell.style.backgroundColor = 'rgb(255, 255, 255)';  
            document.getElementById('log').innerHTML = "cell is disabled";
        }
        
    }
}


function highlightRow(row_id) {
    const row = document.getElementsByClassName("row-" + row_id);
    for (let index = 0; index < 9; index++) {
        row[index].style.backgroundColor = 'rgb(159, 235, 239)';               
    }
}
function clearRowColor(row_id) {
    const row = document.getElementsByClassName("row-" + row_id);
    for (let index = 0; index < 9; index++) {
        if(row[index].disabled == true){
            row[index].style.backgroundColor = 'rgb(238, 238, 238)';               
        }
        else{
            row[index].style.backgroundColor = 'rgb(255, 255, 255)';               
        }
    }
}
function highlightCol(col_id) {
    const row = document.getElementsByClassName("col-" + col_id);
    for (let index = 0; index < 9; index++) {
        row[index].style.backgroundColor = 'rgb(159, 235, 239)';               
    }
}
function clearColColor(col_id) {
    const row = document.getElementsByClassName("col-" + col_id);
    for (let index = 0; index < 9; index++) {
        if(row[index].disabled == true){
            row[index].style.backgroundColor = 'rgb(238, 238, 238)';               
        }
        else{
            row[index].style.backgroundColor = 'rgb(255, 255, 255)';               
        }
    }
}


function colorRowAndCol(cell_id) {
    let row_id = Math.floor(cell_id / 9);
    let col_id = cell_id % 9;
    highlightRow(row_id);
    highlightCol(col_id);
}
function clearRowAndCol(cell_id) {
    let row_id = Math.floor(cell_id / 9);
    let col_id = cell_id % 9;
    clearRowColor(row_id);
    clearColColor(col_id);
}


function onclick(event) {
    clearRedCell();
}

function onmousedown(event) {
    hignlighted_cell = event.target.id.match(/[0-9]+/);
    colorRowAndCol(event.target.id.match(/[0-9]+/));
}


function onmouseup(event) {
    clearRowAndCol(hignlighted_cell);
}
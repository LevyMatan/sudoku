function setCellsIds() {
    // alert("setCellsValue");
    const cells = document.getElementsByClassName("col");
    const num_of_cells = cells.length;
    for (let index = 0; index < num_of_cells; index++) {
        const element = cells[index];
        element.id = "cell-" + index;        
    }
}
function setRowsIds() {
    // alert("setCellsValue");
    const rows = document.getElementsByClassName("row");
    const num_of_rows = rows.length;
    for (let index = 0; index < num_of_rows; index++) {
        const element = rows[index];
        element.id = "row-" + index;        
    }
}

function setColsClass() {
    for (let index = 0; index < 81; index++) {
        const element = document.getElementById("cell-"+index);
        element.classList.add("col--" + index%9);
        // alert("Cell classes are: " + element.className);
    }
}
setCellsIds();
setRowsIds();
setColsClass();
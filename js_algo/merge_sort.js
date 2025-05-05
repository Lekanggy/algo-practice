function merge(arr, startLeft, endLeft, end){
    sizeLeft = endLeft - startLeft + 1
    sizeRight = end - endLeft
    startRight = endLeft + 1

    arrLeft = []
    arrRight = []

    //Copy array into temporay storage
    for(let i = 0; i < sizeLeft; i++){
        arrLeft[i] = arr[startLeft + i]
    }
    arrLeft[sizeLeft] = Number.MAX_SAFE_INTEGER

    for(let i = 0; i < sizeRight; i++){
        arrRight[i] = arr[startRight + i]
    }
    arrRight[sizeRight] = Number.MAX_SAFE_INTEGER


    let indexLeft = 0;
    let indexRight = 0;
    for(let i = startLeft; i <= end; i++ ){
        if(arrLeft[indexLeft] <= arrRight[indexRight]){
            arr[i] = arrLeft[indexLeft]
            indexLeft += 1;
        }else{
            arr[i] = arrRight[indexRight]
            indexRight += 1;
        }
    }

    //console.log("after meger", arr)
}

function mergeSort(arr, start, end){
    if(start < end){
        let endLeft = Math.floor( (start + end ) / 2)
        mergeSort(arr, start, endLeft)
        mergeSort(arr, endLeft + 1, end)
        merge(arr, start, endLeft, end)
    }
}

function mergeSortWrapper(arr){
    let size = arr.length
    mergeSort(arr, 0, size -1)
}


arr = [43, 24, 45, 27, 35, 47, 22, 48]
//merge(arr, 0,3, 7)
//console.log(arr)
mergeSortWrapper(arr)

console.log("run merge", arr)
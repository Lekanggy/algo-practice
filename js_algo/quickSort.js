function exchangeItem(arr, indexA, indexB){
    temp = arr[indexA]
    arr[indexA] = arr[indexB]
    arr[indexB] = temp
}

function partition(array, start, end){
    let pivotValue = array[start]
    let smallIndex = start
    for(let i = start; i <= end; i++){
        if(array[i] < pivotValue){
            smallIndex = smallIndex + 1
            exchangeItem(array, smallIndex, i)
        }
    }

    return smallIndex;
}

function recursiveSort(array, start, end){
    if(start < end){
        let pivotIndex = partition(array, start, end)
        recursiveSort(array, start, pivotIndex - 1)
        recursiveSort(array, pivotIndex + 1, end)
    }
}

function quickSort(array){
    recursiveSort(array, 0, array.length - 1)
}

arr = [43, 24, 45, 27, 35, 47, 22, 48]
//merge(arr, 0,3, 7)
//console.log(arr)
quickSort(arr)

console.log("run sort", arr)
    
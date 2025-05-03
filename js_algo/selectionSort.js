function swapItem(arr, indexA, indexB){
    let temp = arr[indexA]
    arr[indexA] = arr[indexB]
    arr[indexB] = temp
}

function findMin(arr, startIndex){
    let minval = arr[startIndex]
    let minIndx = startIndex
    for(let i = startIndex + 1; i < arr.length; i++ ){
        if(minval > arr[i]){
            minval = arr[i]; // To update the whole arr to arrangfe in decending order just alter this line to minVal  < arr[i]
            minIndx = i
        }
    }

    return minIndx;
}

function selectionSort(arr){
    for (let i = 0; i < arr.length; i++){
        let minIndx = findMin(arr, i)
        console.log(minIndx)
        swapItem(arr, i, minIndx)
    }
}


const arr = [43, 24, 45, 27, 35, 47, 22, 48]

selectionSort(arr)
//swapItem(arr, 0, 7)
//console.log(findMin(arr, 6))
console.log(arr)

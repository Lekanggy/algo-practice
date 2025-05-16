class GenerateRandomNUmber{
    constructor(min=1, max=10){
        this.arr = []
        this.max = max;
        this.min = min;
    }

    #getNumber(){
        let num = Math.floor(Math.random() * (this.max - this.min + 1)) + this.min 
        // let idx = this.arr.indexOf(num)
        // if(idx > -1){
        //     this.arr.splice(idx, 1)
        //     this.#getNumber();
        // }else{
        //     return num
        // }
        return num
    }


    getRandom(){
        let range = (this.max - this.min)
        while(this.arr.length < range){
            let num = this.#getNumber()
            if(num){
                this.arr.push(num)
                console.log(`loading...${Math.floor((this.arr.length / range) * 100)}`)
            };
        }
        
    }
}

const n = new GenerateRandomNUmber(50, 100)

const arr = n.getRandom()

console.log(n.arr)

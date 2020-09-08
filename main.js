console.log('ddddd')
function nn(){
    for(i=0;i<=100;i++){
        console.log(i)
    }

}


function n2(){
    let d='3'
    switch (d){
        case 'chinese':
            console.log('1')
            break;
        case 'korean':
            console.log('korean')
            break;
        case 'filipno':
            console.log('filipno')
            break;
        default :
            console.log('alline')


    }
}

function n3(){
    console.log((!(~+[])+{})[--[~+""][+[]]*[~+[]] + ~~!+[]]+({}+[])[[~!+[]]*~+[]]
    )
}

function n4(i){
    for(let j=10;j>1;j--){
       if (j==i)  {
        console.log(j) 
       }
              
    }

}
// nn();
n2();
// n3();
n4(i=2);

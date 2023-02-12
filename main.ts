let a : number;
let b : boolean;
let c: any;
let e:  number [] ;
enum Color {red = 0, blue = 2, green = 1};
let backgroundColor = Color.red;




let message;
message = 'abc';
let endsWithC = (<string>message).endsWith('c');
let alternativeWay = (message as string).endsWith('c');

// //A little long JS function
// let log = function(message1) {
//   console.log(message1);
// }
// //short TypeScript
// let doLog = () => console.log();



interface Point {
  x: number,
  y: number
}

let drawPoint = (point: Point) => {
  //...
}
drawPoint({
  x : 1,
  y : 2
})

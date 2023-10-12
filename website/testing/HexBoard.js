var layer1 =document.getElementById("myCanvas1"); //tile layer
var ctx1 = layer1.getContext("2d"); //tile context
var board = [];
var mouseX;
var mouseY;
var boardSize;
var tileSize;
var selected;
var hovered;
var held = false;

var layer2 =document.getElementById("myCanvas2"); //selected layer
var ctx2 = layer2.getContext("2d"); //selected context

var layer3 =document.getElementById("myCanvas3"); //selected layer
var ctx3 = layer3.getContext("2d"); //selected context


function Model(source,x,y,width,height) {
    var img;
    this.img = new Image();
    //console.log(this.img);
    this.img.src = source;
    this.x = x;
    this.y = y;
    this.width = width;
    this.height = height;
    this.draw = function() {
	var self = this;
	//this.img.onload = function() {
	    //console.log(self);
	    ctx3.drawImage(self.img,self.x,self.y,self.width,self.height); //200,150,80,160
	//}
    }
}


function getMousePos(canvas, evt) {
    var rect = layer1.getBoundingClientRect();
    return {
        x: evt.clientX - rect.left,
	y: evt.clientY - rect.top
    };
}

layer3.addEventListener('mousedown', function(evt) {
    held = true;
}, false);

layer3.addEventListener('mouseup', function(evt) {
    held = false;
}, false);

layer3.addEventListener('click', function(evt) {
    var mousePos = getMousePos(layer2, evt);
    //alert("working");
    clickContains(mousePos);
        //var message = 'Mouse position: ' + mousePos.x + ',' + mousePos.y;
}, false);

layer3.addEventListener('mousemove', function(evt) {
    var mousePos = getMousePos(layer2, evt);
    if (held)
    {
	dragScreen(mousePos);
	clickContains(mousePos);
    }
    //alert("working");

    mousemoveContains(mousePos);
    mouseX=mousePos.x;
    mouseY=mousePos.y;
        //var message = 'Mouse position: ' + mousePos.x + ',' + mousePos.y;
}, false);


function drawHex(x, y, length, color) {
    var cords = [];
    var angle = 0;
    ctx1.beginPath();
    ctx1.moveTo(x,y);
    for (var i = 0; i < 6; i++) {
	y = y + (Math.cos(angle)*length);
	x = x + (Math.sin(angle)*length);
	ctx1.lineTo(x, y);
	//ctx1.stroke();
	angle = angle + (Math.PI)/3;
	cords.push(x);
	cords.push(y);
    }
    ctx1.fillStyle = color;
    ctx1.fill();
    return cords;
}

function selectHex(perimeter, color) { //Targeted Select vs Highlighted Select
    var i = 2;
    var angle = 0;
    ctx2.beginPath();
    ctx2.moveTo(perimeter[0],perimeter[1]);
    //ctx2.strokeStyle=color;
    while (i < 12) {
	ctx2.lineTo(perimeter[i], perimeter[i+1]);
	//ctx2.stroke();
	angle = angle + (Math.PI)/3;
	i+=2;
    }
    ctx2.lineTo(perimeter[0], perimeter[1]); //getImageData recieves a copy of pixels at that rectangle:
    //ctx2.stroke(); //can be used for checking if clicked character image is transparent
    ctx2.fillStyle = color;
    ctx2.fill();
    return;
}

function highlightHex(perimeter, color) { //Targeted Select vs Highlighted Select
    var i = 2;
    var angle = 0;
    ctx2.beginPath();
    ctx2.moveTo(perimeter[0],perimeter[1]);
    ctx2.strokeStyle=color;
    while (i < 12) {
	ctx2.lineTo(perimeter[i], perimeter[i+1]);
	ctx2.stroke();
	angle = angle + (Math.PI)/3;
	i+=2;
    }
    ctx2.lineTo(perimeter[0], perimeter[1]); //getImageData recieves a copy of pixels at that rectangle:
    ctx2.stroke(); //can be used for checking if clicked character image is transparent
    //ctx2.fillStyle = color;
    //ctx2.fill();
    return;
}


function Hexagon(x,y,length,color,cor1,cor2) {
    this.x = x;
    this.y = y;
    this.length = length;
    this.color = color;
    this.cor1 = cor1;
    this.cor2 = cor2;  //cor2 (floor(j/size) * (j - size + 1))
    var perimeter;
    this.draw = function() {
	this.perimeter = drawHex(this.x,this.y,this.length,this.color).slice(0);
    }
}

function Character(name,icon,model,x,y,team,deck) { 
    this.name = name;
    this.icon = icon;
    this.model = model;
    this.x = x;
    this.y = y;
    this.team = team;
    this.deck = deck;
    var health = 50;
    var energy = 0;
    var hand;
    var discard;
    var effects = [];
    var draw = 3;
    var speed = 3;
    var hand = 3;
    this.draw = function() {
	this.model.draw()
    }
}
    

function clickContains(mouseCords) {
    //var offset1X = mouseCords.x - boardX;
    //var offset1Y = mouseCords.y - boardY;
    //alert(mouseCords.y);
    selected = null;
    for (var i = 0; i < board.length; i++)
    {
	var current = board[i];
	if (typeof current != 'undefined') {
	    //alert(mouseCords.x + "," + mouseCords.y);
	    //alert(current.perimeter[0] + "," + current.perimeter[1]);
	    if ((mouseCords.x > current.perimeter[0] && mouseCords.x < current.perimeter[4]) && (mouseCords.y < current.perimeter[3] && mouseCords.y > current.perimeter[9])
		&& ((mouseCords.y - current.perimeter[11])*Math.sqrt(3)*(-1)) < (mouseCords.x - current.perimeter[10]) && ((mouseCords.y - current.perimeter[7])*Math.sqrt(3)) > ((mouseCords.x - current.perimeter[6])) && ((mouseCords.y - current.perimeter[5])*Math.sqrt(3)*(-1)) > ((mouseCords.x - current.perimeter[4])) && ((mouseCords.y - current.perimeter[1])*Math.sqrt(3)) < ((mouseCords.x - current.perimeter[0])))
	    {
		selected = current;
		//selectHex(current.perimeter, "purple");
		//alert(current.cor1 + "," + current.cor2);
		//console.log(selected);
		return;
	    }
	}
    }
}

function mousemoveContains(mouseCords) {
    //var offset1X = mouseCords.x - boardX;
    //var offset1Y = mouseCords.y - boardY;
    //alert(mouseCords.y);
    hovered = null;
    for (var i = 0; i < board.length; i++)
    {
	var current = board[i];
	if (typeof current != 'undefined') {
	    //alert(mouseCords.x + "," + mouseCords.y);
	    //alert(current.perimeter[0] + "," + current.perimeter[1]);
	    if ((mouseCords.x > current.perimeter[0] && mouseCords.x < current.perimeter[4]) && (mouseCords.y < current.perimeter[3] && mouseCords.y > current.perimeter[9])
		&& ((mouseCords.y - current.perimeter[11])*Math.sqrt(3)*(-1)) < (mouseCords.x - current.perimeter[10]) && ((mouseCords.y - current.perimeter[7])*Math.sqrt(3)) > ((mouseCords.x - current.perimeter[6])) && ((mouseCords.y - current.perimeter[5])*Math.sqrt(3)*(-1)) > ((mouseCords.x - current.perimeter[4])) && ((mouseCords.y - current.perimeter[1])*Math.sqrt(3)) < ((mouseCords.x - current.perimeter[0])))
	    {
		hovered = current;
		//highlightHex(current.perimeter, "purple");
		//alert(current.cor1 + "," + current.cor2);
		//console.log(hovered);
		return;
	    }
	}
    }
}

function dragScreen(mouseCords) { //add list of draggable items later
    var offsetX = mouseCords.x - mouseX;
    var offsetY = mouseCords.y - mouseY;
    avi.x += offsetX; 
    avi.y += offsetY;
    gameBoard.x += offsetX;
    gameBoard.y += offsetY; //specific examples for now
}

function drawHexBoard(x,y,length,width,height,color1,color2) {
    var newX = x;
    var newY = y;
    for (var j = 0; j < height; j++) {
					    
	for (var i = 0; i < width; i++) {
	    if (i % 2 == 0) {
		drawHex(newX,newY,length,color1);
	    }
	    else {
		drawHex(newX,newY+(length*(Math.sqrt(3)/2)),length,color2);
	    }
	    newX+= length*3/2;
	}
	newX = x;
	newY += length*(Math.sqrt(3));
    }
}


function drawHexBoard2(x,y,length,width,height,color1,color2) {
    var newX = x;
    var newY = y;
    for (var j = 0; j < height; j++) {
	//alert(j);
	for (var i = 0; i < width; i++) {
	    alert(i);
	    if (j % 2 == 0) {
		drawHex(newX,newY,length,color1);
	    }
	    else {
		drawHex(newX+(length*(Math.sqrt(3)/2)),newY,length,color2);
	    }
	    newX+= length*(Math.sqrt(3));
	}
	newX = x;
	newY +=  length*3/2;
    }
}

function hexBoard(x,y,length,size,color1,color2) {
    this.x = x;
    this.y = y;
    this.length = length;
    this.size = size;
    this.color1 = color1;
    this.color2 = color2;
    this.draw = function() {
	var self = this;
	drawHexBoardHex(self.x,self.y,self.length,self.size,self.color1,self.color2);
    }
}
	

function drawHexBoardHex(x,y,length,size,color1,color2) {
    board.length = 0;
    var newX = x;
    var newY = y;
    var cordX;
    var cordY;
					    
    for (var j = 0; j < (2*size)-1; j++) {
	//alert(j);
	cordX = j;
	cordY = (Math.floor(j/size) * (1+ j - size));
	for (var i = 0; i < (size + ((size - 1) - Math.abs(((size - 1 - j))))); i++) {
	    // alert("iteration "+ i);
	    //drawHex(newX,newY,length,color1);
	    //alert("board length old:" + board.length);
	    board[board.length] = (new Hexagon(newX,newY,length,color1,cordX,cordY));
	    //alert(board[board.length-1].x);
	    board[board.length -1].draw();
					    
	    cordY+= 1;
	    newX+= length*(Math.sqrt(3));
	}
	newX = x - ((length*(Math.sqrt(3)/2))*((size - 1) - Math.abs(((size - 1) - (j + 1)))));
	newY +=  length*3/2;
    }
} //x is diagonal axis, y is horizontal axis

function drawCycle() {
    ctx1.clearRect(0,0,layer1.width,layer1.height);
    //drawHexBoardHex(125,50,40,6,"green","purple");
    gameBoard.draw();
    //console.log("test");

    ctx2.clearRect(0,0,layer2.width,layer2.height);
    if ((typeof selected != 'undefined') && selected != null)
    {
	selectHex(selected.perimeter, "purple");
	//console.log(selected.perimeter);
    }
    if ((typeof hovered != 'undefined') && hovered != null)
    {
	highlightHex(hovered.perimeter, "blue");
    }

    ctx3.clearRect(0,0,layer3.width,layer3.height);
    hero.draw();
    //console.log(board.length);
    
}

					    					    
					    
//YHex
// drawHex(200,50,25,"red");
//drawHex(200+(25*(Math.sqrt(3))),50,25,"blue");
//drawHex(200+(25*(Math.sqrt(3)/2)),50+37.5,25,"green");
//drawHex(200+(25*(3*Math.sqrt(3)/2)),50+37.5,25,"black");
//XHex
//drawHex(237.5,50+(25*(Math.sqrt(3)/2)),25,"red");
//drawHex(275,50,25,"red");
//drawHex(200,50+(25*(Math.sqrt(3))),25,"red");
//drawHex(237.5,50+(25*(3*Math.sqrt(3)/2)),25,"red");
//drawHex(275,50+(25*(Math.sqrt(3))),25,"red")
//alert(Math.abs(-5));
//board.push(0);
//alert(board[0]);
//drawHexBoard2(20,20,25,4,4,"red","black");
//drawHexBoardHex(125,50,20,7,"green","purple");
var avi = new Model("images/deimoros.png",200,150,100,150);
var hero = new Character("hero","N/A",avi,5,5,"default","N/A");
var gameBoard = new hexBoard(125,50,60,6,"green","red");
//hero.draw();
//console.log(img);

//Play attempt
setInterval(drawCycle,10);

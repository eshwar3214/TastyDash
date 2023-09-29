const express=require('express');

const bodyParser=require('body-parser');

const app=express();

app.use(bodyParser.urlencoded({extended:true}));

var isauthorized=false;

function authorize(req,res,next){
  const studentid=req.body['studentid'];
  const password=req.body['password'];
  if(studentid=="100519733022" && password=="hello"){
    isauthorized=true;

  }
  next();
  
}

app.use(express.static('public'));

app.use(authorize);

app.get('/',(req,res)=>{
 
  res.sendFile('public/index.html');
});

app.get('/haha',(req,res)=>{
  if(isauthorized==true){
    res.send("authorized user");
  }
  else{
    res.send("unauthorized user");
  }
});



app.post('/check',(req,res)=>{

  if(isauthorized==true){
    res.send("authorized");
  }
  else{
    res.send("unauthorized");
  }

});

app.listen(3000,()=>{
  console.log("listening on port 3000");
});



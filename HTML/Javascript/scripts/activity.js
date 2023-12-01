document.getElementById("myButton").addEventListener("click", function() {
    alert("Button clicked!");
    });

    function myFunction() {
        alert("Button clicked!");
    }
document.getElementById("betterButton").addEventListener("click", myFunction);
    
    function calculate_grade(){
    let grades = document.getElementById("gradeInput").value;
    let lettergrade = grade(grades)
    alert("Calculate Letter Grade:- " + lettergrade)
}

function grade(grades){
    if (grades >= 90){
        return "A+";
    }else if (grades >= 85){
        return "A";
    }else if (grades >= 80){
        return "A-";
    }else if (grades >= 77){
        return "B+";
    }else if (grades >= 73){
        return "B";
    }else if (grades >= 70){
        return "B-";
    }else if (grades >= 67){
        return "C+";
    }else if (grades >= 63){
        return "C";
    }else if (grades >= 60){
        return "C-";
    }else if (grades >= 55){
        return "D+";
    }else if (grades >= 50){
        return "D";
    }else{
        return "F";
    }
}
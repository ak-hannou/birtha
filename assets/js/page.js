function fn(){

    var u35 = false;
    var o35 = false;

    var smokeY = false;
    var smokeN = false;

    var pcos = false;
    var pdd = false;
    var endo = false;
    var acne = false;

    var hair = false;
    var depress = false;
    var mood = false;
    var nausea = false;
    var bleed = false;

    var clots = false;
    var cancer = false;
    var heart = false;
    var migraines = false;
    var pressure = false;
    var diabetes = false;

    var clona = false;
    var topi = false;
    var mela = false;
    var pred = false;
    var lora = false;
    var amit = false;
    var metform = false;

    var month = false;
    var skip = false;
    var matter = false;

    var radio1 = document.getElementsByName('customRadioInline1-1-2');
    if(radio1[0].checked){
        u35 = true;
    }
    else if(radio1[1].checked){
        o35 = true;
    }

    var radio2 = document.getElementsByName('customRadioInline1-3-4');
    if(radio2[0].checked){
        smokeY = true;
    }
    else if(radio2[1].checked){
        smokeN = true;
    }

    var radio3 = document.getElementsByName('condtions1');
    if(radio3[0].checked){
        pcos = true;
    }
    if(radio3[1].checked){
        pdd = true;
    }
    if(radio3[2].checked){
        endo = true;
    }
    if(radio3[3].checked){
        acne = true;
    }

    var radio4 = document.getElementsByName('effects1');
    if(radio4[0].checked){
        hair = true;
    }
    if(radio4[1].checked){
        depress = true;
    }
    if(radio4[2].checked){
        mood = true;
    }
    if(radio4[3].checked){
        nausea = true;
    }
    if(radio4[4].checked){
        bleed = true;
    }

    var radio5 = document.getElementsByName('experiences1');
    if(radio5[0].checked){
        clots = true;
    }
    if(radio5[1].checked){
        cancer = true;
    }
    if(radio5[2].checked){
        heart = true;
    }
    if(radio5[3].checked){
        migraines = true;
    }
    if(radio5[4].checked){
        pressure = true;
    }
    if(radio5[5].checked){
        diabetes = true;
    }

    var radio6 = document.getElementsByName('meds1');
    if(radio6[0].checked){
        clona = true;
    }
    if(radio6[1].checked){
        topi = true;
    }
    if(radio6[2].checked){
        mela = true;
    }
    if(radio6[3].checked){
        pred = true;
    }
    if(radio6[4].checked){
        lora = true;
    }
    if(radio6[5].checked){
        amit = true;
    }
    if(radio6[6].checked){
        metform = true;
    }

    var radio7 = document.getElementsByName('customRadioInline');
    if(radio7[0].checked){
        month = true;
    }
    else if(radio7[1].checked){
        skip = true;
    }
    else if(radio7[2].checked){
        matter = true;
    }


    if(o35 && smokeY || (clots||cancer||heart||migraines||pressure||diabetes)){
        location.href = "minipill.html";
    }

    else if(endo){
        location.href = "previfem.html";
    }
    else if(pcos){
        location.href = "alesse.html";
    }
    else if(pdd){
        location.href = "beyaz.html";
    }
    else if(acne){
        if(topi){
            location.href = "gianvi.html";
        }
        else {
            location.href = "ocella.html";
        }
    }
    else if(skip){
        var rand = Math.floor(Math.random() * 2);
        if(rand==1){
            location.href = "seasonique.html";
        }
        else{
            location.href = "seasonale.html";
        }
    }
    else if(clona || topi || mela || pred || lora || amit || metform){
        location.href = "velivet.html";
    }
    else if(hair || depress || mood || nausea || bleed ){
        location.href = "apri.html";
    }
    else {
        location.href = "lybrel.html";
    }




}
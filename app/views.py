from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def form(request):
    
    return HttpResponse('''
<head>
   
    <title>Student Details</title>
</head>
<body>
   <form action="">
    <fieldset>
         <legend>Student Details</legend>
         <table>
            <tr>
                <td><lable for="">Student Name</lable></td>
                <td><input type="text" placeholder="enter the student name"></td>
                <td><lable for="">Father Name</lable></td>
                <td><input type="text" placeholder="enter the fathername"></td>
                <td><lable for="">Mother Name</lable></td>
                <td><input type="text" placeholder="enter the mothername"></td>
                
            </tr>
            <tr>
                <td><lable for="datepicker">Date of birth</lable></td>
                <td><input type="date"></td>
            </tr>
            <tr>
                <td><lable>Gender</lable></td>
                <td><input type="radio">Male</td>
                <td> <input type="radio">Female</td>
                <td><input type="radio">Others</td>
            </tr>
            <tr>
                <td><lable for="">Mobile no.</lable></td>
                <td><input type="text" placeholder="enter the mob.no."></td>
            </tr>
            <tr>
                <td><lable for="">Email</lable></td>
                <td><input type="text" placeholder="enter the email"></td>
            </tr>
               <tr>
                <td><lable for="">Address</lable></td>
                <td><textarea name="" id="cols="20" rows="5"></textarea></text></textarea></td>
               </tr>
               <tr>
                <td><label for="">State</label></td>
                <td><select id="States">
                    <option value="">select</option>
                    <option value="">Andhra Pradesh</option>
                    <option value="">Arunachal Pradesh</option>
                    <option value="">Bihar</option>
                    <option value="">Chhattisgharh</option>
                    <option value="">Jharkhand</option>
                    <option value="">Karnatak</option>
                    <option value="">Kerala</option>
                    <option value="">Odisa</option>
                    <option value="">Gujrat</option>
                    <option value="">Goa</option>
                    <option value="">Haryana</option>
                    <option value="">Panjab</option>
                    <option value="">Uttar Pradesh</option>
                    <option value="">Uttarakhand</option>

                </select></td>
               </tr>
                <tr>
                    <td><lable>Language</lable></td>
                    <td><input type="checkbox">Hindi</td>
                    <td> <input type="checkbox">English</td>
                    <td><input type="checkbox">Telgu</td>
                    <td><input type="checkbox">Odiya</td>
                </tr>
                <tr>
                    <td><lable>Choose file</lable></td>
                    <td><input type=""placeholder="Choose file"></td>
                </tr>
                <tr align="center">
                    <td><button>Reset</button></td>
                    <td><button>Submit</button></td>
                </tr>
         </table>
    </fieldset>
   </form>
</body>
</html>
   ''')

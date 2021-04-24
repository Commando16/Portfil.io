from flask import Flask, render_template, redirect, request, session
import os
import shutil
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import requests







BaseDir = os.path.dirname(__file__)

app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = os.path.join(BaseDir,"uploads")

app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:@localhost/portfolioproject'
db = SQLAlchemy(app)



#DB Model
class About_data(db.Model):
    sno     = db.Column(db.Integer, primary_key=True, unique=True)
    user_id = db.Column(db.String(50), unique=True)
    text    = db.Column(db.Integer, primary_key=False)


class Acadmic_data(db.Model):
    sno       = db.Column(db.Integer, primary_key=True, unique=True)
    user_id   = db.Column(db.String(50), unique=True)
    course    = db.Column(db.String(50), primary_key=False)
    duration  = db.Column(db.String(25), primary_key=False)
    institute = db.Column(db.String(100), primary_key=False)


class Achievement_data(db.Model):
    sno     = db.Column(db.Integer, primary_key=True, unique=True)
    user_id = db.Column(db.String(50), unique=True)
    image   = db.Column(db.String(), primary_key=False)
    tag     = db.Column(db.String(30), primary_key=False)


class Experience_data(db.Model):
    sno          = db.Column(db.Integer, primary_key=True, unique=True)
    user_id      = db.Column(db.String(50), unique=True)
    designation  = db.Column(db.String(50), primary_key=False)
    duration     = db.Column(db.String(25), primary_key=False)
    organisation = db.Column(db.String(), primary_key=False)
    discription  = db.Column(db.String(), primary_key=False)


class Link_data(db.Model):
    sno     = db.Column(db.Integer, primary_key=True, unique=True)
    user_id = db.Column(db.String(50), unique=True)
    name    = db.Column(db.String(50), unique=True)
    link    = db.Column(db.String, primary_key=False)


class Profile_data(db.Model):
    sno      = db.Column(db.Integer, primary_key=True, unique=True)
    user_id  = db.Column(db.String(50), unique=True)
    image    = db.Column(db.String(), primary_key=False)
    name     = db.Column(db.String(30), primary_key=False)
    mobile   = db.Column(db.String(12), primary_key=False)
    email    = db.Column(db.String(100), primary_key=False)
    location = db.Column(db.String(), primary_key=False)


class Project_data(db.Model):
    sno          = db.Column(db.Integer, primary_key=True, unique=True)
    user_id      = db.Column(db.String(50), unique=True)
    image        = db.Column(db.String(), primary_key=False)
    description  = db.Column(db.String(), primary_key=False)
    link         = db.Column(db.String(), primary_key=False)


class Skill_data(db.Model):
    sno         = db.Column(db.Integer, primary_key=True, unique=True)
    user_id     = db.Column(db.String(50), unique=True)
    skill_name  = db.Column(db.String(50), primary_key=False)


class Totals(db.Model):
    sno   = db.Column(db.Integer, primary_key=True, unique=True)
    name  = db.Column(db.String(50), unique=True)
    total = db.Column(db.Integer, primary_key=False)












#file checker class
class filechecker():
    
    def __init__(self):
        pass

    # function for checking for correct file extension
    def isAllowed(self, file_name, allowed_extension):
        file_extension = file_name.rsplit('.', 1)[1].lower()
        return ( file_extension in allowed_extension )






#global variables 
ALLOWED_IMAGE_EXTENSION = ['jpg', 'png', 'jpeg']
FILE_CHECK = filechecker()

CURRENT_TIMESTAMP = datetime.now()
CURRENT_DAY = str(CURRENT_TIMESTAMP.day)
CURRENT_MONTH = str(CURRENT_TIMESTAMP.month)
CURRENT_YEAR = str(CURRENT_TIMESTAMP.year)
CURRENT_TIME = str(CURRENT_TIMESTAMP)[11:]








# debug print statement
print("the upload dir is",app.config['UPLOAD_FOLDER'])

#---------- page routes ----------

# index page route
@app.route('/')
def LoginPage():
    return render_template('Login.html')
    

# AdminPannel pannel route
@app.route('/AdminPanel')
def UploadPannel():
    if session['LoginStatus'] == 'LoggedIn':
        return render_template("AdminPanel.html")
    else:
        return redirect("/")

# Profile pagae route
@app.route('/Profile/<user_id>', methods=['GET'])
def Profile(user_id):
    if request.method == 'GET':
        return user_id
    else:
        # return sorry
        pass




#---------- form handlers routes ----------

#login form handler
@app.route('/LoginFormHandler', methods=['POST'])
def LoginFormHandler():
    if request.method == 'POST':
        #fetching and setting up data in local variable
        username = request.form['inputUser']
        password = request.form['inputPassword']

        if ( username == "Admin" and password == "Password" ):
            session['LoginStatus'] = 'LoggedIn'
            session['id'] = '1'
            return redirect("/AdminPanel")
        else:
            return redirect("/")


#logout form handler
@app.route('/LogoutFormHandler', methods=['POST'])
def LogoutFormHandler():
    session.pop('LoginStatus')
    return redirect("/")











# Profile Form Handler 
@app.route('/ProfileFormHandler', methods=['POST'])
def ProfileFormHandler():
    if request.method == 'POST':
        profile_image = request.files['profileImageInp']
        profile_name = request.form['profilenameInp']
        profile_mobile = request.form['profilemobileInp']
        profile_email = request.form['profileemailInp']
        profile_location = request.form['profilelocationInp']

        print("*************************")
        print(profile_image, profile_name, profile_mobile, profile_email, profile_location)
        print("*************************")

        totalfetch = Totals.query.filter_by(name="profile_data").all()
        currenttotal = totalfetch[0].total
        newtotal = currenttotal + 1

        finalfilename = str(newtotal)+'_'+secure_filename(profile_image.filename)
        ActualUploaddirectory = os.path.join(app.config['UPLOAD_FOLDER'],"ProfilePhotoUploads")

        if not os.path.exists( ActualUploaddirectory ):
            os.makedirs( ActualUploaddirectory )

        if finalfilename.split(".")[-1].lower() in ['jpg', 'jpeg', 'png']:
            #Extension = finalfilename.split(".")[-1] 

            finalpath = os.path.join( ActualUploaddirectory , finalfilename )

            profile_image.save( finalpath )


            Profile_data_entry = Profile_data( user_id = session['id'], image = finalpath, name = profile_name, mobile = profile_mobile, email = profile_email, location = profile_location)
            db.session.add(Profile_data_entry)
            db.session.commit()


            Total_data_entry = Totals.query.filter_by(name="profile_data").first()
            Total_data_entry.total = newtotal
            db.session.commit()
        
        else:
            return "file formate not allowed."


        return "profile form submitted"
                
    else:
        return redirect("/")


# Skill Form Handler
@app.route('/SkillFormHandler', methods=['POST'])
def SkillFormHandler():
    if request.method == 'POST':
        skill_name = request.form['skillsTextInp']

        print("*************************")
        print(skill_name)
        print("*************************")

        entry = Skill_data( user_id = session['id'], skill_name = skill_name )
        db.session.add(entry)
        db.session.commit()
        

        return "skill form submitted"
           
    else:
        return redirect("/")

    
# Link Form Handler
@app.route('/LinkFormHandler', methods=['POST'])
def LinkFormHandler():
    if request.method == 'POST':
        link_name = request.form['linkLabelInp']
        link_link = request.form['linkLinkInp']

        print("*************************")
        print(link_name, link_link)
        print("*************************")

        entry = Link_data( user_id = session['id'], name = link_name, link = link_link )
        db.session.add(entry)
        db.session.commit()

        return "Link form submitted"
        
    else:
        return redirect("/")


# About Form Handler
@app.route('/AboutFormHandler', methods=['POST'])
def AboutFormHandler():
    if not session.get("id") is None:
        if request.method == 'POST':
            about_text = request.form['aboutMeTextInp']

            print("*************************")
            print(about_text)
            print("*************************")

            entry = About_data( user_id = session['id'], text = about_text)
            db.session.add(entry)
            db.session.commit()

            return "about form submitted"
        
        else:
            return redirect("/")
    else:
            return redirect("/")    
    
# Experience Form Handler
@app.route('/ExperienceFormHandler', methods=['POST'])
def ExperienceFormHandler():
    if not session.get("id") is None:
        if request.method == 'POST':
            experience_designation = request.form['experiencedesignationTextInp']
            experience_duration = request.form['experiencedateTextInpFrom']+" - "+request.form['experiencedateTextInpTo']
            experience_organisation = request.form['experiencecompanyTextInp']
            experience_description = request.form['experiencejobDescriptionTextInp']

            print("*************************")
            print(experience_designation, experience_duration, experience_organisation, experience_description)
            print("*************************")

            entry = Experience_data( user_id = session['id'], designation = experience_designation , duration = experience_duration , organisation = experience_organisation , discription = experience_description)
            db.session.add(entry)
            db.session.commit()

            return "experience form submitted"

            
        else:
            return redirect("/")
    else:
            return redirect("/")
    
# Acadmic Form Handler
@app.route('/AcadmicFormHandler', methods=['POST'])
def AcadmicFormHandler():
    if not session.get("id") is None:
        if request.method == 'POST':
            acadmic_course = request.form['acadmicqualificationTextInp']
            acadmic_institute = request.form['acadmicinstituteTextInp']
            acadmic_duration= request.form['acadmicdateTextInpFrom']+" - "+request.form['acadmicdateTextInpTo']
            

            print("*************************")
            print(acadmic_course, acadmic_duration, acadmic_institute)
            print("*************************")

            entry = Acadmic_data( user_id = session['id'], course = acadmic_course, duration = acadmic_institute , institute = acadmic_duration )
            db.session.add(entry)
            db.session.commit()

            return "acadmic form submitted"
        else:
            return redirect("/")

    else:
            return redirect("/")

# Achievement Form Handler
@app.route('/AchievementFormHandler', methods=['POST'])
def AchievementFormHandler():
    if not session.get("id") is None:
        if request.method == 'POST':
            achievement_image = request.files['certificateImageFileInp']
            achievement_tag   = request.form['certificateTextInp']


            print("*************************")
            print( achievement_image , achievement_tag )
            print("*************************")
            
            totalfetch = Totals.query.filter_by(name="acadmic_data").all()
            currenttotal = totalfetch[0].total
            newtotal = currenttotal + 1


            finalfilename = str(newtotal)+'_'+secure_filename(achievement_image.filename)
            ActualUploaddirectory = os.path.join(app.config['UPLOAD_FOLDER'],"AchievementUploads")

            if not os.path.exists( ActualUploaddirectory ):
                os.makedirs( ActualUploaddirectory )

            if finalfilename.split(".")[-1].lower() in ['jpg', 'jpeg', 'png']:
                    #Extension = finalfilename.split(".")[-1] 

                    finalpath = os.path.join( ActualUploaddirectory , finalfilename )

                    achievement_image.save( finalpath )


                    entry = Achievement_data( user_id = session['id'], image = finalpath , tag = achievement_tag )
                    db.session.add(entry)
                    db.session.commit()

                    Total_data_entry = Totals.query.filter_by(name="acadmic_data").first()
                    Total_data_entry.total = newtotal
                    db.session.commit()

            return "achievement form submitted"
            
        else:
            return redirect("/")
    
    else:
            return redirect("/")

    
# Project Form Handler
@app.route('/ProjectFormHandler', methods=['POST'])
def ProjectFormHandler():
    if not session.get("id") is None:
        if request.method == 'POST':
            project_name = request.form['projectNameTextInp']
            project_image = request.files['projectImageFileInp']
            project_description = request.form['projectDescriptionTextInp']
            project_link = request.form['projectLinkTextInp']

            print("*************************")
            print( project_name, project_image, project_description, project_link )
            print("*************************")

            totalfetch = Totals.query.filter_by(name="project_data").all()
            currenttotal = totalfetch[0].total
            newtotal = currenttotal + 1

            finalfilename = str(newtotal)+'_'+secure_filename(project_image.filename)
            ActualUploaddirectory = os.path.join(app.config['UPLOAD_FOLDER'],"ProjectUploads")

            if not os.path.exists( ActualUploaddirectory ):
                os.makedirs( ActualUploaddirectory )

            if finalfilename.split(".")[-1].lower() in ['jpg', 'jpeg', 'png']:
                #Extension = finalfilename.split(".")[-1] 

                finalpath = os.path.join( ActualUploaddirectory , finalfilename )

                project_image.save( finalpath )


                Project_data_entry = Project_data( user_id = session['id'], image = finalpath , description = project_description, link = project_link)
                db.session.add(Project_data_entry)
                db.session.commit()

                Total_data_entry = Totals.query.filter_by(name="project_data").first()
                Total_data_entry.total = newtotal
                db.session.commit()

            

            return "project form submitted"
            
        else:
            return redirect("/")
    else:
            return redirect("/")



























'''
# Notification Form Handler 
@app.route('/NotificationFormHandler', methods=['POST'])
def NotificationFormHandler():
    if request.method == 'POST':

        # fetching and setting up data in local variables
        notificationTextInp = request.form['notificationTextInp']
        date = CURRENT_DAY+"-"+CURRENT_MONTH+"-"+CURRENT_YEAR+" "+CURRENT_TIME

        # retriving the data form Totals collection about total notification
        total_notification_doc_reference = db.collection(u'Totals').document(u'notifications')
        total_notification = total_notification_doc_reference.get().to_dict()
        total_notification = total_notification["total"]


        # debuging print statement
        print("got the notification text as - ",notificationTextInp," ", date)
        
        # incrementing the total count in variable
        new_notifiction_count = total_notification + 1

        # inserting the data in a new document 
        notification_doc_reference = db.collection(u'Notification').document(str(new_notifiction_count))
        notification_doc_reference.set({
            u'date': date,
            u'notification': notificationTextInp,
        })

        # incrementing the new element count by updating the notification document in Totals collection
        total_notification_doc_reference = db.collection(u'Totals').document(u'notifications')
        total_notification_doc_reference.set({
            u'total': new_notifiction_count,
        })
        
        return ("the notification text reached. "+notificationTextInp + " total notification now are"+str(total_notification+1))


# Image Form Pannel
@app.route('/ImageFormHandler', methods=['POST'])
def ImageFormHandler():
    if request.method == 'POST':

        # fetching the data in the local variable 
        imageLabelInp = request.form['imageLabelInp']
        uploadedimagefile = request.files['imageFileInp']
        print(uploadedimagefile)

        # fetching the data form the Totals collection image document
        total_image_doc_reference = db.collection(u'Totals').document(u'photo')
        total_image = total_image_doc_reference.get().to_dict()
        total_image = total_image["total"]

        # incrementing the total count in variable
        new_image_count = total_image + 1

        # checking for correct/acceptable image file extension
        if(FILE_CHECK.isAllowed( uploadedimagefile.filename, ALLOWED_IMAGE_EXTENSION )):
            
            # determining the path to store file and making if not exist
            
            dir_path = os.path.join(app.config['UPLOAD_FOLDER'],'UploadImages',str(new_image_count))
            if not os.path.exists(dir_path):
                os.mkdir(dir_path)
            

            path = os.path.join(app.config['UPLOAD_FOLDER'],'UploadImages',str(new_image_count),uploadedimagefile.filename)
            uploadedimagefile.save(path)
            

            # uploading image on firebase Storage
          
            fileprefix = "UploadedImage_"+str(new_image_count)+"_"
            
            fileName = uploadedimagefile.filename
            fullfilename = "UploadedImage_" + str(new_image_count) + "_" + fileName
            bucket = storage.bucket()
            blob = bucket.blob(fullfilename)
            blob.upload_from_filename(path)

            # to give the public access to a file
            blob.make_public()
            print("************************************")
            print(type(blob.public_url))
            print("************************************")

            # inserting the data in a new document 
            image_doc_reference = db.collection(u'Photo').document(str(new_image_count))
            image_doc_reference.set({
                u'label': imageLabelInp,
                u'path': fullfilename,
            })

            # debug print statment
            print("got the notification text as - ",imageLabelInp)

            # incrementing the new element count by updating the notification document in Totals collection
            total_image_doc_reference = db.collection(u'Totals').document(u'photo')
            total_image_doc_reference.set({
                u'total': new_image_count,
            })

            # removing the file copy from the local storage.
            shutil.rmtree(dir_path)

            return ("the image file reached. "+"<a href='"+blob.public_url+"'>link</a>")
        
        else:
            return ("this file extesion is not allowed to be uploaded")


# Video Form Pannel
@app.route('/VideoLinkFormHandler', methods=['POST'])
def VideoLinkFormHandler():
    if request.method == 'POST':

        # fetching the data in the local variable 
        videoLabelInp = request.form['videoLabelInp']
        videoLinkInp = request.form['videoLinkInp']

        # fetching the data form the Totals collection video document
        total_video_doc_reference = db.collection(u'Totals').document(u'videos')
        total_video = total_video_doc_reference.get().to_dict()
        total_video = total_video["total"]

        # incrementing the total count in variable
        new_video_count = total_video + 1


        # inserting the data in a new document 
        video_doc_reference = db.collection(u'Video').document(str(new_video_count))
        video_doc_reference.set({
            u'label': videoLabelInp,
            u'link': videoLinkInp,
        })

        # incrementing the new element count by updating the notification document in Totals collection
        total_video_doc_reference = db.collection(u'Totals').document(u'videos')
        total_video_doc_reference.set({
            u'total': new_video_count,
        })
       
        # debug print statment
        print(videoLabelInp," ",videoLinkInp)

        return (videoLabelInp+" "+videoLinkInp)

        
# Music Form Pannel
@app.route('/MusicFormHandler', methods=['POST'])
def MusicFormHandler():
    if request.method == 'POST':
        musicLabelInp = request.form['musicLabelInp']
        uploadedMusicFile = request.files['musicFileInp']

        # fetching the data form the Totals collection music document
        total_music_doc_reference = db.collection(u'Totals').document(u'musics')
        total_music = total_music_doc_reference.get().to_dict()
        total_music = total_music["total"]

        # incrementing the total count in variable
        new_music_count = total_music + 1

         # checking for correct/acceptable music file extension
        if(FILE_CHECK.isAllowed( uploadedMusicFile.filename, ALLOWED_MUSIC_EXTENSION )):

            # determining the path to store file and making if not exist
            dir_path = os.path.join(app.config['UPLOAD_FOLDER'],'UploadMusic',str(new_music_count))
            if not os.path.exists(dir_path):
                os.mkdir(dir_path)

            path = os.path.join(app.config['UPLOAD_FOLDER'],'UploadMusic',str(new_music_count),uploadedMusicFile.filename)
            uploadedMusicFile.save(path)

            # uploading image on firebase Storage
            fileName = uploadedMusicFile.filename
            fullfilename = "UploadedMusic_" + str(new_music_count) + "_" + fileName
            bucket = storage.bucket()
            blob = bucket.blob(fullfilename)
            blob.upload_from_filename(path)

            # to give the public access to a file
            blob.make_public()
            print("************************************")
            print(type(blob.public_url))
            print("************************************")


            # inserting the data in a new document 
            music_doc_reference = db.collection(u'Music').document(str(new_music_count))
            music_doc_reference.set({
                u'label': musicLabelInp,
                u'path': fullfilename,
            })

            # incrementing the new element count by updating the notification document in Totals collection
            total_music_doc_reference = db.collection(u'Totals').document(u'musics')
            total_music_doc_reference.set({
                u'total': new_music_count,
            })
        
            # removing the file copy from the local storage.
            shutil.rmtree(dir_path)

            print(musicLabelInp)
            return ("the music file reached. "+"<a href='"+blob.public_url+"'>link</a>")
        
        else:
            return ("this file extesion is not allowed to be uploaded")


# Text Story Form Pannel
@app.route('/TextStoryFormHandler', methods=['POST'])
def TextStoryFormHandler():
    if request.method == 'POST':
        StoryTextInp = request.form['StoryTextInp']    
        date = CURRENT_DAY+"-"+CURRENT_MONTH+"-"+CURRENT_YEAR+" "+CURRENT_TIME

        # retriving the data form Totals collection about total stories
        total_stories_doc_reference = db.collection(u'Totals').document(u'stories')
        total_stories = total_stories_doc_reference.get().to_dict()
        total_stories = total_stories["total"]

        # incrementing the total count in variable
        new_stories_count = total_stories + 1

        # inserting the data in a new document 
        stories_doc_reference = db.collection(u'Story').document(str(new_stories_count))
        stories_doc_reference.set({
            u'date': date,
            u'data': StoryTextInp,
            u'type': u'text',
        })

        # incrementing the new element count by updating the notification document in Totals collection
        total_stories_doc_reference = db.collection(u'Totals').document(u'stories')
        total_stories_doc_reference.set({
            u'total': new_stories_count,
        })

        # debug print statement
        print(StoryTextInp)

        return (StoryTextInp)


# Image Story Form Pannel
@app.route('/ImageStoryFormHandler', methods=['POST'])
def ImageStoryFormHandler():
    if request.method == 'POST':
        # fetching the data in the local variable 
        uploadedstoryimagefile = request.files['StoryImageInp']
        date = CURRENT_DAY+"-"+CURRENT_MONTH+"-"+CURRENT_YEAR+" "+CURRENT_TIME

        # retriving the data form Totals collection about total stories
        total_stories_doc_reference = db.collection(u'Totals').document(u'stories')
        total_stories = total_stories_doc_reference.get().to_dict()
        total_stories = total_stories["total"]

        # incrementing the total count in variable
        new_stories_count = total_stories + 1

        if(FILE_CHECK.isAllowed( uploadedstoryimagefile.filename, ALLOWED_IMAGE_EXTENSION )):
            
            # determining the path to store file and making if not exist
            dir_path = os.path.join(app.config['UPLOAD_FOLDER'],'UploadStoryImage',str(new_stories_count))
            if not os.path.exists(dir_path):
                os.mkdir(dir_path)

            path = os.path.join(app.config['UPLOAD_FOLDER'],'UploadStoryImage',str(new_stories_count),uploadedstoryimagefile.filename)
            uploadedstoryimagefile.save(path)

            # uploading image on firebase Storage
            fileName = uploadedstoryimagefile.filename
            fullfilename = "UploadedStoryImage_" + str(new_stories_count) + "_" + fileName
            bucket = storage.bucket()
            blob = bucket.blob(fullfilename)
            blob.upload_from_filename(path)

            # to give the public access to a file
            blob.make_public()
            print("************************************")
            print(type(blob.public_url))
            print("************************")

            # inserting the data in a new document 
            stories_doc_reference = db.collection(u'Story').document(str(new_stories_count))
            stories_doc_reference.set({
                u'date': date,
                u'data': fullfilename,
                u'type': u'image',
            })

            # incrementing the new element count by updating the notification document in Totals collection
            total_stories_doc_reference = db.collection(u'Totals').document(u'stories')
            total_stories_doc_reference.set({
                u'total': new_stories_count,
            })

            # removing the file copy from the local storage.
            shutil.rmtree(dir_path)

            return ("the story image uploaded successfully.")
        
        else:
            return ("this file extesion is not allowed to be uploaded.")


'''









if __name__ == '__main__':
    app.debug = True
    app.run()


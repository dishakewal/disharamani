from django.shortcuts import render,redirect
from django.conf import settings
from .models import User,Area,Wishlist,Cart
from django.core.mail import send_mail
import random

def home(request):
	return render(request,'home.html')


def signup(request):
	if request.method=="POST":
		try:
			user=User.objects.get(email=request.POST['email'])
			msg="User already Registered!!"
			return render(request,"signup.html",{msg:'msg'})
		except:
			if request.POST['password']==request.POST['cpassword']:
				User.objects.create(
					firstname=request.POST['firstname'],
					lastname=request.POST['lastname'],
					email=request.POST['email'],
					mobile=request.POST['mobile'],
					gender=request.POST['gender'],
					address=request.POST['address'],
					password=request.POST['password'],
					cpassword=request.POST['cpassword'],
					image=request.FILES['image'],
					usertype=request.POST['usertype']
					)
				msg="Signup Successfully!!"
				return render(request,"home.html",{msg:'msg'})
			else:
				msg="Incorrect password!!"
				return render(request,"signup.html",{msg:'msg'})

	else:
		return render(request,"signup.html")

def login(request):
	if request.method=="POST":
		try:
			user=User.objects.get(
				email=request.POST['email'],
				password=request.POST['password']
				)
			if user.usertype=="user":
				request.session['email']=user.email
				request.session['firstname']=user.firstname
				request.session['image']=user.image.url
				return render(request,"home.html")
			elif user.usertype=="seller":
				request.session['email']=user.email
				request.session['firstname']=user.firstname
				request.session['image']=user.image.url
				return render(request,"sellerhome.html")

		except Exception as e:
			print("Exception : --------------------------------------",e)
			msg="email and password are incorrect"
			return render(request,"login.html",{'msg':msg})
	else:

		return render(request,"login.html")

def logout(request):
	try:
		del request.session['email']
		del request.session['firstname']
		del request.session['image']
		return render(request,'login.html')
	except:
		return redirect("logout")
# Create your views here.
def  Userupdateprofile(request):
		user=User.objects.get(email=request.session['email'])
		if request.method=="POST":
			user.firstname=request.POST['firstname']
			user.lastname=request.POST['lastname']
			user.email=request.POST['email']
			user.mobile=request.POST['mobile']
			user.gender=request.POST['gender']
			user.address=request.POST['address']
			user.password=request.POST['password']
			user.cpassword=request.POST['cpassword']
			try:
				user.image=request.FILES['image']
				user.save()
			except:
				pass
			user.save()
			msg="Update Successfully!!"
			return render(request,"Userupdateprofile.html",{'msg':msg})
		else:
			
			return render(request,"Userupdateprofile.html",{"user":user})	

def forgot_passwd(request):
	if request.method=='POST':
		try:
			subject = 'otp for registration!!'
			otp=random.randint(1000,9999)
			message = 'hi user, your otp is: '+str(otp)
			email_from = settings.EMAIL_HOST_USER
			recipient_list = [request.POST['email'], ]
			send_mail( subject, message, email_from, recipient_list )
			return render(request,"otp.html",{'otp':otp,'email':request.POST['email']})
		except:
			msg="email doesnt match!!"
			return render(request,"forgot_passwd.html",{"msg":msg})
	else:
		return render(request,"forgot_passwd.html")

def otp(request):
		otp1=request.POST['otp1']
		otp2=request.POST['otp2']
		email=request.POST['email']

		if otp1==otp2:
			user=User.objects.get(email=email)
			user.status="active"
			user.save()
			msg="otp verified successfully!!"
			return render(request,'new_password.html',{'msg':msg,'email':email})
		else:
			msg="invalid otp"
			return render(request,"otp.html",{'otp':otp1,'email':request.POST['email'], 'msg':msg})

def new_password(request):
	email=request.POST['email']
	npassword=request.POST['npassword']
	cpassword=request.POST['cnewpassword']

	user=User.objects.get(email=email)

	if npassword==cpassword:
		user.password=npassword
		user.cpassword=npassword
		user.save()
		msg="password change successfully"
		return render(request,"login.html",{"msg":msg})
	else:
		msg="password doeasnt match"
		return render(request,"new_password.html",{"msg":msg})
	return render(request,"new_password.html")

def change_password(request):
	if request.method=="POST":
		user=User.objects.get(email=request.session['email'])


		if user.password==request.POST['oldpassword']:
			if request.POST['newpassword']==request.POST['cnpassword']:
				user.password=request.POST['newpassword']
				user.cnpassword=request.POST['newpassword']
				user.save()
				return redirect('logout')
			else: 
				msg="password dosent match"
				return render (request,'change_password.html',{'msg':msg})	
		else:
			msg="old password inncorrect"
			return render (request,'change_password.html',{'msg':msg})
	else:
		return render (request,'change_password.html')

def sellerhome(request):
	return render(request,"sellerhome.html")


def sellersignup(request):
	if request.method=="POST":
		try:
			user=User.objects.get(email=request.POST['email'])
			msg="User already Registered!!"
			return render(request,"signup.html",{msg:'msg'})
		except:
			if request.POST['password']==request.POST['cpassword']:
				User.objects.create(
					firstname=request.POST['firstname'],
					lastname=request.POST['lastname'],
					email=request.POST['email'],
					mobile=request.POST['mobile'],
					gender=request.POST['gender'],
					address=request.POST['address'],
					password=request.POST['password'],
					cpassword=request.POST['cpassword'],
					image=request.FILES['image'],
					usertype=request.POST['usertype']
					)
				msg="Signup Successfully!!"
				return render(request,"login.html",{msg:'msg'})
			else:
				msg="Incorrect password!!"
				return render(request,"sellersignup.html",{msg:'msg'})

	else:
		return render(request,"sellersignup.html")

def sellerprofile(request):
	user=User.objects.get(email=request.session['email'])
	if request.method=="POST":
		user.firstname=request.POST['firstname']
		user.lastname=request.POST['lastname']
		user.email=request.POST['email']
		user.mobile=request.POST['mobile']
		user.ender=request.POST['gender']
		user.address=request.POST['address']
		user.password=request.POST['password']
		user.cpassword=request.POST['cpassword']
		try:
			user.image=request.FILES['image']
			user.save()
		except:
			pass
		user.save()
		return render(request,"sellerprofile.html")
	else:

		return render(request,"sellerprofile.html",{"user":user})

def sellerchange_password(request):
	if request.method=="POST":
		user=User.objects.get(email=request.session['email'])

		if user.password==request.POST['oldpassword']:
			if request.POST['newpassword']==request.POST['cnpassword']:
				user.password=request.POST['newpassword']
				user.cnpassword=request.POST['newpassword']
				user.save()
				return redirect('logout')

			else: 
				msg="password dosent match"
				return render (request,'sellerchange_password.html',{'msg':msg})	
		else:
			msg="old password inncorrect"
			return render (request,'sellerchange_password.html',{'msg':msg})
	else:
		return render (request,'sellerchange_password.html')


def seller_adddetails(request):
	if request.method=="POST":
		try:
			seller=User.objects.get(email=request.session['email'])
			Area.objects.create(
				seller=seller,
				Area=request.POST['Area'],
				Address=request.POST['Address'],
				Looking_To=request.POST['Looking_To'],
				Property_Kind=request.POST['Property_Kind'],
				Property_Layout=request.POST['Property_Layout'],
				Property_Ownership=request.POST['Property_Ownership'],
				Super_Area=request.POST['Super_Area'],
				facing_road=request.POST['facing_road'],
				Property_Flooring=request.POST['Property_Flooring'],
				Water_source=request.POST['Water_source'],
				Facing=request.POST['Facing'],
				Furnishing=request.POST['Furnishing'],
				Property_id=request.POST['Property_id'],
				Price=request.POST['Price'],
				Additional_Details=request.POST['Additional_Details'],
				Contact=request.POST['Contact'],
				Image1=request.FILES['Image1'],
				Image2=request.FILES['Image2'],
				Image3=request.FILES['Image3'],
				Image4=request.FILES['Image4'],
				Image5=request.FILES['Image5'],
				)
			msg="Added Successfully!!"
			return render(request,"seller_adddetails.html",{'msg':msg})
		except:
			a=Area.objects.get(email=request.session['email'])
			if a>2:
				return render(request,"mycart.html")	
			else:
				return render(request,"seller_adddetails.html")		
		
	else:
		return render(request,"seller_adddetails.html")

def seller_viewdetails(request):
	seller=User.objects.get(email=request.session['email'])
	area=Area.objects.filter(seller=seller)
	return render(request,"seller_viewdetails.html",{'area':area})

def seller_moredetails(request,pk):
	area=Area.objects.get(pk=pk)
	return render(request,"seller_moredetails.html",{'area':area})

def seller_Editdetails(request,pk):
	area=Area.objects.get(pk=pk)
	if request.method=="POST":
		area.Area=request.POST['Area']
		area.Looking_To=request.POST['Looking_To']
		area.Property_Kind=request.POST['Property_Kind']
		area.Property_Layout=request.POST['Property_Layout']
		area.Property_Ownership=request.POST['Property_Ownership']
		area.Super_Area=request.POST['Super_Area']
		area.facing_road=request.POST['facing_road']
		area.Property_Flooring=request.POST['Property_Flooring']
		area.Water_source=request.POST['Water_source']
		area.Facing=request.POST['Facing']
		area.address=request.POST['Address']
		area.Furnishing=request.POST['Furnishing']
		area.Property_id=request.POST['Property_id']
		area.Price=request.POST['Price']
		area.Additional_Details=request.POST['Additional_Details']
		area.Contact=request.POST['Contact']
		try:
			area.Image1=request.FILES['Image1']
			area.Image2=request.FILES['Image2']
			area.Image3=request.FILES['Image3']
			area.Image4=request.FILES['Image4']
			area.Image5=request.FILES['Image5']
			area.save()
		except:
			pass
		area.save()		
		return redirect("seller_viewdetails")
	else:
		return render(request,"seller_Editdetails.html",{'area':area})

def seller_Deletedetails(request,pk):
	area=Area.objects.get(pk=pk)
	area.delete()
	return redirect("seller_viewdetails")

def ahmd_area(request):
	return render(request,"ahmd_area.html")

def user_view_all_details(request,aa):
	if aa=='All':
		area=Area.objects.all()
		return render (request,'user_view_all_details.html',{'area':area})
	else:
		area=Area.objects.filter(Area=aa)
		return render(request,'user_view_all_details.html',{'area':area})

def user_moredetails(request,pk):
	flag=False
	flag1=False
	area=Area.objects.get(pk=pk)
	user=User.objects.get(email=request.session['email'])

	try:
		Wishlist.objects.get(user=user,area=area)
		flag=True
	except:
		pass

	try:
		Cart.objects.get(user=user,area=area)
		flag1=True
	except:
		pass
	return render (request,'user_moredetails.html',{'area':area, 'flag':flag , 'flag1':flag1})

def add_to_wishlist(request,pk):
	area=Area.objects.get(pk=pk)
	user=User.objects.get(email=request.session['email'])
	Wishlist.objects.create(user=user,area=area)
	return redirect('mywishlist')

def mywishlist(request):
	user=User.objects.get(email=request.session['email'])
	wishlist=Wishlist.objects.filter(user=user)
	request.session['wishlist_count']=len(wishlist)
	return render(request,'mywishlist.html',{'wishlist':wishlist})

def remove_from_wishlist(request,pk):
	area=Area.objects.get(pk=pk)
	user=User.objects.get(email=request.session['email'])
	wishlist=Wishlist.objects.get(user=user,area=area)
	wishlist.delete()
	return redirect('mywishlist')

def  add_to_cart(request,pk):
	area=Area.objects.get(pk=pk)
	user=User.objects.get(email=request.session['email'])
	Cart.objects.create(user=user,area=area,Price=area.Price,total_price=area.Price)
	return redirect('mycart')

def mycart(request):
	net_price=0
	user=User.objects.get(email=request.session['email'])
	cart=Cart.objects.filter(user=user)
	for i in cart:
		net_price=net_price+i.total_price
	request.session['cart_count']=len(cart)
	return render(request,'mycart.html',{'cart':cart,'net_price':net_price})

def remove_from_cart(request,pk):
	area=Area.objects.get(pk=pk)
	user=User.objects.get(email=request.session['email'])
	cart=Cart.objects.get(user=user,area=area)
	cart.delete()
	return redirect('mycart')

def change_qty(request,pk):
	cart=Cart.objects.get(pk=pk)
	cart.total_price=cart.price
	cart.save()
	return redirect('mycart')


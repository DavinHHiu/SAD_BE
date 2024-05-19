from django.contrib.auth.hashers import make_password, check_password
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from userapp.models import User, Account, FullName, Address
from userapp.serializers import LoginSerializer, UserSerializer, UserProfileSerialier


class RegisterUserApiView(APIView):
    def post(self, request):
        password = request.data["password"]
        password = make_password(password)
        account = Account(username=request.data["username"], password=password)
        user = User(email=request.data["email"], account=account)
        response = user.is_valid()
        if response["status"] == status.HTTP_201_CREATED:
            account.save()
            user.save()
            serializer = UserSerializer(user)
            return Response(serializer.data, status=response["status"])
        else:
            return Response(response["message"], status=response["status"])


class LoginUserApiView(APIView):
    def post(self, request):
        data = request.data
        account = Account.objects.filter(username=data["username"]).first()
        print(account)
        if account:
            input_password = data["password"]
            if check_password(input_password, account.password):
                user = User.objects.filter(account=account).first()
                return Response({"user_id": user.id}, status=status.HTTP_200_OK)

        return Response(
            {"message": "Tài khoản hoặc mật khẩu không đúng"},
            status=status.HTTP_400_BAD_REQUEST,
        )


class UserProfileApiView(APIView):
    def get_object(self, user_id):
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            return None

    def post(self, request):
        user_id = request.data.get("user_id")
        print(user_id)
        user = self.get_object(user_id)
        if user is not None:
            serializer = UserProfileSerialier(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(
                {"res": "User with user_id does not exist"},
                status=status.HTTP_404_NOT_FOUND,
            )

    def put(self, request):
        data = request.data
        user = self.get_object(data["id"])
        print(data)
        if user is not None:
            if user.account:
                password = (
                    data["password"].strip()
                    if data["password"].strip()
                    else user.account.password
                )
                password = make_password(password)
                account = Account(
                    id=user.account.id,
                    username=data["username"],
                    password=password,
                )
            else:
                account = Account(username=data["username"], password=data["password"])
            if user.fullname:
                fullname = FullName(
                    id=user.fullname.id,
                    firstname=data["firstname"],
                    lastname=data["lastname"],
                )
            else:
                fullname = FullName(
                    firstname=data["firstname"], lastname=data["lastname"]
                )
            if user.address:
                address = Address(
                    id=user.address.id,
                    street=data["street"],
                    district=data["district"],
                    city=data["city"],
                )
            else:
                address = Address(
                    street=data["street"],
                    district=data["district"],
                    city=data["city"],
                )
            response = user.is_valid(is_update=True)
            if response["status"] == status.HTTP_201_CREATED:
                account.save()
                fullname.save()
                address.save()
                user = User(
                    id=data["id"],
                    email=data["email"],
                    account=account,
                    fullname=fullname,
                    address=address,
                )
                user.save()
                serializer = UserProfileSerialier(user)
                return Response(serializer.data, status=response["status"])
            else:
                return Response(response["message"], status=response["status"])

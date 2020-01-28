from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import psycopg2

try:
        conn = psycopg2.connect(        user='lvdbzgnnnthckg',
                                        password= '7ef0652e2f717ff49f5369871183b2dcdd15d9c52a7c55fcef98779d410dcb10',
                                        host = 'ec2-184-72-237-95.compute-1.amazonaws.com',
                                        port = '5432',
                                        database = 'd32b9rckhe5166',

                                        )
        cursor = conn.cursor()


except (Exception, psycopg2.Error) as error:

        print ("error while connecting to postgres")



class GetConn(APIView):

    def get(self,request):
        cursor.execute('Select * from portal_jobs where owner_id=1')
        rec = cursor.fetchall()
        cursor.execute('select username from auth_user where id=1')
        usr_name = cursor.fetchone()

        return Response ({'user':usr_name,'Jobs posted':rec})

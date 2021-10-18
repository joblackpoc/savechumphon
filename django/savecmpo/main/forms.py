from django import forms
from main.models import Ctambon, Savecmpo

class InputForm(forms.ModelForm):

    class Meta:
        model = Savecmpo

        fields = (
            'fname','lname','gender','age','id_card','mobile_phone','mobile_partner','date_arrive','date_leave','Cchangwat'
            ,'campur','ctambon','moo','house','duty','vaccine_pic','sickness','lab'
        )

        labels = {
            'fname':'ชื่อ'
            ,'lname':'นามสกุล'
            ,'gender':'เพศ'
            ,'age':'อายุ'
            ,'id_card':'เลขประชาชน/พาสปอร์ต/ประกันสังคม'
            ,'mobile_phone':'เบอร์โทรศัพท์มือถือ'
            ,'mobile_partner':'เบอร์โทรศัพท์มือถือคนใกล้ชิด'
            ,'date_arrive':'วันที่มาถึงชุมพร'
            ,'date_leave':'วันที่ออกจากชุมพร'
            ,'Cchangwat':'มาจากจังหวัด'
            ,'campur':'อำเภอที่พักในชุมพร'
            ,'ctambon':'ตำบลที่พักในชุมพร'
            ,'moo':'หมู่บ้าน ถนน อาคาร ตึก ร้านค้า โรงแรม ที่พัก ถนน'
            ,'house':'บ้านเลขที่ ห้องพักเลขที่'
            ,'duty':'เหตุผลในการเดินทางมาชุมพร'
            ,'vaccine_pic':'ใบรับรองการฉีดวัคซีน'
            ,'sickness':'ใบรับรองแพทย์ป่วยโควิด-19 ไม่เกิน 90 วัน'
            ,'lab':'ใบรับรองผลการตรวจหาเชื้อโควิด-19'
        }

        widgets = {
            'fname': forms.TextInput(attrs={'placeholder':'ชื่อตามบัตรประชาชน'})
            ,'lname':forms.TextInput(attrs={'placeholder':'นามสกุล'})
            ,'gender':forms.Select(attrs={'placeholder':'เพศ'})
            ,'age':forms.TextInput(attrs={'placeholder':'อายุ'})
            ,'id_card':forms.TextInput(attrs={'placeholder':'เลขประจำตัวประชาชน'})
            ,'mobile_phone':forms.TextInput(attrs={'placeholder':'เบอร์โทรศัพท์มือถือ'})
            ,'mobile_partner':forms.TextInput(attrs={'placeholder':'เบอร์โทรศัพท์มือถือคนใกล้ชิด'})
            ,'date_arrive':forms.SelectDateWidget(attrs={'placeholder':'วันที่เดินทางมาถึงชุมพร'})
            ,'date_leave':forms.SelectDateWidget(attrs={'placeholder':'วันที่เดินทางออกจากชุมพร'})
            ,'moo':forms.TextInput(attrs={'placeholder':'หมู่บ้าน ถนน อาคาร ตึก ร้านค้า โรงแรม ที่พัก ถนน'})
            ,'house':forms.TextInput(attrs={'placeholder':'บ้านเลขที่ ห้องพักเลขที่'})
            ,'duty':forms.Select(attrs={'placeholder':'เหตุผลในการเดินทาง'})

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['ctambon'].queryset=Ctambon.objects.none()

        if 'campur' in self.data:
            try:
                ampurcodefull = int(self.data.get('campur'))
                self.fields['ctambon'].queryset=Ctambon.objects.filter(ampurcode_id=ampurcodefull).order_by('tambonname')
            except(ValueError,TypeError):
                pass            

        elif self.instance.pk:
            self.fields['ctambon'].queryset = self.instance.campur.ctambon_set.order_by('tambonname')

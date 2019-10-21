from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model
from django import forms

elective_subjects = [(11, '생활과 윤리'), (12, '윤리와 사상'), (13, '한국 지리'), (14, '세계 지리'), (15, '동아시아사'), (16, '세계사'), (17, '법과 정치'), (18, '경제'), (19, '사회·문화'),\
                    (21, '물리I'), (22, '물리II'), (23, '화학I'), (24, '화학II'), (25, '생명과학I'), (26, '생명과학II'), (27, '지구과학I'), (28, '지구과학II')]
languages = list(enumerate(['선택 안 함', '독일어Ⅰ', '프랑스어Ⅰ', '스페인어Ⅰ', '중국어Ⅰ', '일본어Ⅰ', '러시아어Ⅰ', '아랍어Ⅰ', '베트남어Ⅰ', '한문Ⅰ']))


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('nickname', 'dream_univ', 'curriculum', 'elective_subject1', 'elective_subject2', 'second_foreign_lang')
        labels = {
            'nickname': '닉네임',
            'dream_univ': '목표대학',
            'curriculum': '계열',
            'elective_subject1': '선택과목1',
            'elective_subject2': '선택과목2',
            'second_foreign_lang': '제2외국어',
        }
        widgets = {
            'dream_univ': forms.TextInput(
                attrs={
                    'placeholder': '예시) OO대학교'
                }
            ),
            'curriculum': forms.Select(
                choices=[(1, '문과'), (2, '이과'), (3, '예체능')]
            ),
            'elective_subject1': forms.Select(
                choices=elective_subjects
            ),
            'elective_subject2': forms.Select(
                choices=elective_subjects
            ),
            'second_foreign_lang': forms.Select(
                choices=languages
            )
        }

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'nickname', 'dream_univ', 'curriculum', 'elective_subject1', 'elective_subject2', 'second_foreign_lang')
        labels = {
            'nickname': '닉네임',
            'dream_univ': '목표대학',
            'curriculum': '계열',
            'elective_subject1': '선택과목1',
            'elective_subject2': '선택과목2',
            'second_foreign_lang': '제2외국어',
        }
        widgets = {
            'dream_univ': forms.TextInput(
                attrs={
                    'placeholder': '예시) OO대학교'
                }
            ),
            'curriculum': forms.Select(
                choices=[(1, '문과'), (2, '이과'), (3, '예체능')]
            ),
            'elective_subject1': forms.Select(
                choices=elective_subjects
            ),
            'elective_subject2': forms.Select(
                choices=elective_subjects
            ),
            'second_foreign_lang': forms.Select(
                choices=languages
            )
        }
from django import forms


class MemberAreaForm(forms.Form):
    login_username = forms.CharField(label_suffix='', label='Usuário', max_length=51, required=False)
    password_username = forms.CharField(label_suffix='', label='Senha', max_length=36, widget=forms.PasswordInput, required=False)
    username = forms.CharField(label_suffix='', label='Nome de usuário', max_length=51, required=True)
    passw = forms.CharField(label_suffix='', label='Senha', max_length=36, widget=forms.PasswordInput, required=True)
    confirmpass = forms.CharField(label_suffix='', label='Confirmar senha', max_length=36, widget=forms.PasswordInput, required=True)
    name = forms.CharField(label_suffix='', label='Nome', max_length=100, required=True)
    cpf = forms.CharField(label_suffix='', label='CPF', max_length=11, required=True)
    phone = forms.CharField(label_suffix='', label='Telefone', max_length=20, required=True)
    email = forms.EmailField(label_suffix='', label='Email', max_length=75, required=True)
from flask import Flask, render_template, request

app = Flask(__name__)

class PendeteksiKankerPayudara:
    def __init__(self, tekstur, perimeter, kehalusan, kekompakan, simetri, dimensi_fraktal):
        self.tekstur = tekstur
        self.perimeter = perimeter
        self.kehalusan = kehalusan
        self.kekompakan = kekompakan
        self.simetri = simetri
        self.dimensi_fraktal = dimensi_fraktal

    def analisis_fitur(self):
        hasil = self.tekstur * 0.5 + self.perimeter * 0.3 + self.kehalusan * 0.2
        return hasil

    def deteksi_kanker(self):
        hasil_analisis = self.analisis_fitur()

        if hasil_analisis > 0.7:
            return "Deteksi kanker payudara positif"
        else:
            return "Deteksi kanker payudara negatif"


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        tekstur = float(request.form['tekstur'])
        perimeter = float(request.form['perimeter'])
        kehalusan = float(request.form['kehalusan'])
        kekompakan = float(request.form['kekompakan'])
        simetri = float(request.form['simetri'])
        dimensi_fraktal = float(request.form['dimensi_fraktal'])

        data_pasien = PendeteksiKankerPayudara(tekstur, perimeter, kehalusan, kekompakan, simetri, dimensi_fraktal)

        hasil = data_pasien.deteksi_kanker()

        return render_template('hasil.html', hasil=hasil)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

from app import db
from datetime import datetime, timezone

class Iventory(db.Model):
    id_iventory = db.Column(db.Integer, primary_key = True, autoincrement= True)
    nama_barang = db.Column(db.String(200), nullable=False, index=True)
    jumlah_barang = db.Column(db.Integer, nullable=True,)
    kondisi_barang = db.Column(db.String(200), nullable=False)
    jumlah_barang_rusak = db.Column(db.Integer, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    update_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))

    def __repr__(self) -> str:
        return f'<Iventory {self.nama_barang}'
    
    def to_dict(self):
        return {
            'id':self.id_iventory,
            'nama_barang':self.nama_barang,
            'jumlah_barang':self.jumlah_barang,
            'kondis_barang':self.kondisi_barang,
            'jumlah_barang_rusak':self.jumlah_barang_rusak,
            'created_at':self.created_at,
            'update_at':self.update_at
        }

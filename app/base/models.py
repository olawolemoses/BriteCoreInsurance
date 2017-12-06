# Define a base model for other database tables to inherit
from app import db

from marshmallow import Schema, fields, pprint

# Define a base model for other database tables to inherit
class Base(db.Model):

    __abstract__  = True

    id            = db.Column(db.Integer, primary_key=True)
    date_created  = db.Column(db.DateTime,  default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime,  default=db.func.current_timestamp(),
                                           onupdate=db.func.current_timestamp())
    
class RiskType(Base):
    
    __tablename__ = 'risk_type'
        
    riskType = db.Column(db.String(80), unique=True, nullable=False)
    riskFields = db.relationship("RiskField", backref="risk_type",  lazy='dynamic')
    
    def __init__(self, riskType):

        self.riskType = riskType
        
    def __repr__(self):
        
        return '<Risk %r>' % self.riskType

class RiskFieldType(Base):
    
    __tablename__ = 'risk_field_type'
    
    fieldType = db.Column(db.String(80), unique=True, nullable=False)
    
    def __init__(self, fieldType):

        self.fieldType = fieldType
        
    def __repr__(self):
        
        return '<RiskFieldType %r>' % self.fieldType

class RiskField(Base):
    
    __tablename__ = 'risk_field'
    
    riskTypeId = db.Column(db.Integer, db.ForeignKey('risk_type.id'), nullable=False)
        
    riskFieldTypeId = db.Column(db.Integer, db.ForeignKey('risk_field_type.id'), nullable=False)
    
    riskField = db.Column(db.String(80), nullable=False)
    
    riskType = db.relationship('RiskType', backref='risk_fields', lazy=True)

    type = db.relationship('RiskFieldType', backref='risk_field_types')
    
    def __init__(self, riskTypeId, riskFieldTypeId, riskField):

        self.riskTypeId = riskTypeId
        
        self.riskFieldTypeId = riskFieldTypeId
        
        self.riskField = riskField

    def __repr__(self):
        
        return '<RiskField %r>' % self.riskField


class RiskFieldTypeSchema(Schema):
    id = fields.Int()
    fieldType = fields.Str()

class RiskFieldSchema(Schema):
    id = fields.Int()
    riskField = fields.Str()
    type = fields.Nested(RiskFieldTypeSchema)
        
class RiskTypeSchema(Schema):
    id = fields.Int()
    riskType = fields.Str()
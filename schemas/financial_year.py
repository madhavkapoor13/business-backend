from pydantic import BaseModel

class FinancialYearCreate(BaseModel):
    start_year: int
    end_year: int

class ShowFinancialYear(BaseModel):
    financial_year_id: int
    start_year: int
    end_year: int

    class Config:
        from_attributes = True
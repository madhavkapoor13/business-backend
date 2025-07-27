from pydantic import BaseModel


class ProvisionBase(BaseModel):
    entity_id: int
    department_id: int
    financial_year_id: int
    quarter_id: int
    item_id: int
    quantity: int
    approx_price: float
    remarks: str
    is_special_provisioning: bool
    is_budget_frozen: bool
    created_by: str


class ShowProvision(BaseModel):
    id: int  # changed from provisioning_id
    entity_id: int
    department_id: int
    financial_year_id: int
    quarter_id: int
    item_id: int
    quantity: int
    approx_price: float
    remarks: str
    is_special_provisioning: bool
    is_budget_frozen: bool
    created_by: str

    class Config:
        from_attributes = True  # FastAPI v2+


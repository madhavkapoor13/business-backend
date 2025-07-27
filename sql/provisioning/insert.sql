INSERT INTO provisioning (
    entity_id,
    department_id,
    financial_year_id,
    quarter_id,
    item_id,
    quantity,
    approx_price,
    remarks,
    is_special_provisioning,
    is_budget_frozen,
    created_by
) VALUES (
    :entity_id,
    :department_id,
    :financial_year_id,
    :quarter_id,
    :item_id,
    :quantity,
    :approx_price,
    :remarks,
    :is_special_provisioning,
    :is_budget_frozen,
    :created_by
);

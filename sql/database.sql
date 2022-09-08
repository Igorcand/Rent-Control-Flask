Table users {
  id int PK
  name varchar
  username varchar
  email varchar
  password varchar
}

Table address {    
  id int PK
  street varchar
  number int
  city varchar
  state varchar
  country varchar
  zipcode int
  user_id int 
}

Table tenant {    
  id int PK
  name varchar
  age int
  cpf int
  phone int
  payment float
  entry int
  email varchar 
  activate boolean
  user_id int
}

Table property {    
  id int PK
  name varchar
  iptu int
  value float
  pendency boolean
  address_id int
  tenant_id int
  user_id int
  
}

Ref {
  users.id > address.user_id
}

Ref {
  users.id > tenant.user_id
}

Ref {
  users.id > property.user_id
}

Ref {
  address.id > property.address_id
}

Ref {
  tenant.id > property.tenant_id
}

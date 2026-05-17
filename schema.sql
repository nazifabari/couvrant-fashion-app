create table clothing_categories(
	id SERIAL primary key,
	name TEXT not null unique 
);

create table design_tags(
	id SERIAL primary key,
	name TEXT not null unique 
);

create table sizes(
id SERIAL primary key,
size TEXT not null unique
);

create table items(
    id SERIAL primary key,
    name TEXT not null,
    description TEXT,
    price NUMERIC not null,
    currency TEXT not null, 
    brand_name TEXT not null,
    product_url TEXT not null,
    color TEXT not null,
    category_id INTEGER not null references clothing_categories(id),
    in_stock BOOLEAN not null,
    source TEXT not null,
    external_id TEXT not null,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW() 
);

create table item_tags(
	item_id INTEGER not null references items(id),
    tag_id INTEGER not null references design_tags(id),
    PRIMARY KEY (item_id, tag_id)
);

create table item_sizes(
	item_id INTEGER not null references items(id),
    size_id INTEGER not null references sizes(id),
    PRIMARY KEY (item_id, size_id)
);

create table images(
	id SERIAL PRIMARY key,	
	image_url TEXT not null,
	item_id INTEGER not null references items(id),
	image_type TEXT not null,
	is_display_image BOOLEAN not null default false, 
	display_order INTEGER 
	);
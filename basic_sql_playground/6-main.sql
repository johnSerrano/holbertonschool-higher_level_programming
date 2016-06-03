select name, sum(age)
from person
join tvshowperson
join (
	select name, id as tv_id
	from tvshow
)
where id = person_id
and tv_id = tvshow_id
group by tvshow_id;

select name, first_name, last_name, min(age)
from person
join tvshowperson
join (
	select name, id as tv_id
	from tvshow
)
where id = person_id
and tv_id = tvshow_id
group by tvshow_id;

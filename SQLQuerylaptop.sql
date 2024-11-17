								--- DATA TRANSFORMATION --- 

begin transaction ;

update [dbo].[StagingWarehouse] set ScreenSize = '15.6 Inch'
where ScreenSize like '15%' ;
commit

select * from [dbo].[StagingWarehouse]
WHERE CPU = 'Intel Iris xe'


begin transaction ;
update [dbo].[StagingWarehouse] set ScreenSize = '14 Inch'
where CPU = 'M3 Pro' 
commit


begin transaction ;
update [dbo].[StagingWarehouse] set Price = REPLACE(Price,',','')
where Price like '%LE';
commit


begin transaction ;
update [dbo].[StagingWarehouse] set GPU = 'Qualcomm Adreno'
where GPU = 'Qualcomm Adren'
commit

select distinct(GPU) from [dbo].[StagingWarehouse]


begin transaction ;
update [dbo].[StagingWarehouse] set CPU = 'AMD Ryzen 5-7520U'
where CPU = 'AMD RyzenR5-7520U'
commit



begin transaction
UPDATE [dbo].[StagingWarehouse]
SET CPU = STUFF(CPU, 11, 1, '')
where CPU like 'AMD Ryzen R%'

rollback 

begin transaction ;
update [dbo].[StagingWarehouse] set CPU = REPLACE(CPU,'R',' ')
where CPU like'AMD Ryzen%'
rollback
commit


select * from [dbo].[StagingWarehouse]
where GPU = 'AMD Ryzen 9'

begin transaction 
delete from [dbo].[StagingWarehouse] 
where CPU = 'Intel Core 7-150U '
commit


select * from [dbo].[StagingWarehouse]


begin transaction ;
update [dbo].[StagingWarehouse] set GPU = REPLACE(GPU,'Integrated','')
commit

alter table [dbo].[laptop_warehouse]
alter column Price nvarchar(max) not null

BEGIN TRANSACTION;

INSERT INTO [dbo].[laptop_warehouse]
SELECT *
FROM [dbo].[StagingWarehouse];

COMMIT;

select * from [dbo].[laptop_warehouse]


delete from [dbo].[laptop_warehouse]



from fastapi import HTTPException
from tortoise.exceptions import DoesNotExist

from src.db.models import Notes
from src.db.schemas.datasets import NoteOutSchema


async def get_datasets():
    return await NoteOutSchema.from_queryset(Notes.all())


async def get_datasets(dataset_id) -> NoteOutSchema:
    return await NoteOutSchema.from_queryset_single(Datasets.get(id=dataset_id))


async def create_dataset(dataset, user) -> NoteOutSchema:
    dataset_dict = dataset.dict(exclude_unset=True)
    dataset["user.id"] = user.id
    dataset_obj = await Notes.create(**dataset_dict)
    return await NoteOutSchema.from_tortoise_orm(dataset_obj)


async def update_dataset(dataset_id, dataset) -> NoteOutSchema:
    try:
        dataset_db = await NoteOutSchema.from_queryset_single(Notes.get(id=dataset_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"Dataset {dataset_db} not found")

    if db_note.author.id == current_user.id:
        await Notes.filter(id=note_id).update(**note.dict(exclude_unset=True))
        return await NoteOutSchema.from_queryset_single(Notes.get(id=note_id))

    raise HTTPException(status_code=403, detail=f"Not authorized to update")


async def delete_note(note_id, current_user):
    try:
        db_note = await NoteOutSchema.from_queryset_single(Notes.get(id=note_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"Note {note_id} not found")

    if db_note.author.id == current_user.id:
        deleted_count = await Notes.filter(id=note_id).delete()
        if not deleted_count:
            raise HTTPException(status_code=404, detail=f"Note {note_id} not found")
        return f"Deleted note {note_id}"

    raise HTTPException(status_code=403, detail=f"Not authorized to delete")
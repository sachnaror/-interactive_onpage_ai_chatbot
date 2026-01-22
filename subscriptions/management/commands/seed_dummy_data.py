from django.core.management.base import BaseCommand
from subscriptions.models import SubscriptionDocument
from datetime import date

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        SubscriptionDocument.objects.all().delete()

        for i in range(1, 21):
            SubscriptionDocument.objects.create(
                user_name="Sachin",
                offering_name=f"Offering {i}",
                profile_name="CG" if i % 2 == 0 else "LLC",
                document_name=f"Investment Agreement {i}.pdf",
                status="eSign Completed" if i % 3 != 0 else "Pending",
                executed_on=date(2025, 11, i) if i % 3 != 0 else None,
                download_url=f"/download/{i}" if i % 4 != 0 else None,
            )

        self.stdout.write("✅ Seeded 20 dummy records")

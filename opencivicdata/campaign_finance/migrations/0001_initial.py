# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-11-06 22:21
from __future__ import unicode_literals

import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import opencivicdata.core.models.base
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('elections', '0007_auto_20171022_0234'),
        ('core', '0004_auto_20171005_2028'),
    ]

    operations = [
        migrations.CreateModel(
            name='Committee',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='The date and time of creation.')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='The date and time of the last update.')),
                ('extras', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, help_text='A key-value store for storing arbitrary information not covered elsewhere.')),
                ('locked_fields', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, default=list, size=None)),
                ('id', opencivicdata.core.models.base.OCDIDField(ocd_type='campaign-finance-committee', serialize=False, validators=[django.core.validators.RegexValidator(flags=32, message='ID must match ^ocd-campaign-finance-committee/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', regex='^ocd-campaign-finance-committee/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$')])),
                ('name', models.CharField(help_text='The name of the Committee.', max_length=300)),
                ('image', models.URLField(blank=True, help_text='A URL leading to an image that identifies the Committee visually.', max_length=2000)),
                ('ballot_measure_options_supported', models.ManyToManyField(db_table='opencivicdata_committeeballotmeasureoptionsupported', help_text='Ballot Measure Options for which the Committee declared support.', related_name='supporting_committees', to='elections.BallotMeasureContestOption')),
            ],
            options={
                'db_table': 'opencivicdata_committee',
            },
        ),
        migrations.CreateModel(
            name='CommitteeCandidacyDesignation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(choices=[('supports', 'Supports'), ('opposes', 'Opposes'), ('primary-vehicle-for', 'Primary vehicle for'), ('surplus-account-for', 'Surplus account for'), ('independent-expenditure', 'Independent Expenditure')], help_text='Describes the relationship betweent the Committee and Candidacy.', max_length=10)),
                ('candidacy', models.ForeignKey(help_text='Reference to a Candidacy with the which the Committee has a designated relationship.', on_delete=django.db.models.deletion.CASCADE, related_name='committees', to='elections.Candidacy')),
                ('committee', models.ForeignKey(help_text='Reference to a Committee with the which the Candidacy has a designated relationship.', on_delete=django.db.models.deletion.CASCADE, related_name='candidacy_designations', to='campaign_finance.Committee')),
            ],
            options={
                'db_table': 'opencivicdata_committeecandidacydesignation',
            },
        ),
        migrations.CreateModel(
            name='CommitteeIdentifier',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('identifier', models.CharField(help_text='A unique identifier developed by an upstream or third party source.', max_length=300)),
                ('scheme', models.CharField(help_text='The name of the service that created the identifier.', max_length=300)),
                ('committee', models.ForeignKey(help_text='Reference to the Committee identified by this alternative identifier.', on_delete=django.db.models.deletion.CASCADE, related_name='identifiers', to='campaign_finance.Committee')),
            ],
            options={
                'db_table': 'opencivicdata_committeeidentifier',
            },
        ),
        migrations.CreateModel(
            name='CommitteeName',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(db_index=True, help_text='An alternative name.', max_length=500)),
                ('note', models.CharField(blank=True, help_text='A short, optional note about alternative name.', max_length=500)),
                ('start_date', models.CharField(blank=True, help_text='An optional start date for usage of the alternative name in YYYY[-MM[-DD]] string format.', max_length=10)),
                ('end_date', models.CharField(blank=True, help_text='An optional end date for usage of the alternative name in YYYY[-MM[-DD]] string format.', max_length=10)),
                ('committee', models.ForeignKey(help_text='A link to the Committee with this alternative name.', on_delete=django.db.models.deletion.CASCADE, related_name='other_names', to='campaign_finance.Committee')),
            ],
            options={
                'db_table': 'opencivicdata_committeename',
            },
        ),
        migrations.CreateModel(
            name='CommitteeSource',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('note', models.CharField(blank=True, help_text='A short, optional note related to an object.', max_length=300)),
                ('url', models.URLField(help_text='A hyperlink related to an object.', max_length=2000)),
                ('committee', models.ForeignKey(help_text='Reference to the Committee this source verifies.', on_delete=django.db.models.deletion.CASCADE, related_name='sources', to='campaign_finance.Committee')),
            ],
            options={
                'db_table': 'opencivicdata_committeesource',
            },
        ),
        migrations.CreateModel(
            name='CommitteeStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classification', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100), help_text='Classification for the status, such as "active" or "contesting election".', size=None)),
                ('note', models.CharField(blank=True, help_text='Description of the status', max_length=300)),
                ('start_date', models.CharField(help_text='First date at which the status applied (inclusive).', max_length=10)),
                ('end_date', models.CharField(blank=True, help_text=' Last date at which the status applied (inclusive). In many cases, the current status won’t have a known end_date associated with it.', max_length=10)),
                ('committee', models.ForeignKey(help_text='Reference to the Committee.', on_delete=django.db.models.deletion.CASCADE, related_name='statuses', to='campaign_finance.Committee')),
            ],
            options={
                'db_table': 'opencivicdata_committeestatus',
            },
        ),
        migrations.CreateModel(
            name='CommitteeType',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='The date and time of creation.')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='The date and time of the last update.')),
                ('extras', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, help_text='A key-value store for storing arbitrary information not covered elsewhere.')),
                ('locked_fields', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, default=list, size=None)),
                ('id', opencivicdata.core.models.base.OCDIDField(ocd_type='campaign-finance-committee-type', serialize=False, validators=[django.core.validators.RegexValidator(flags=32, message='ID must match ^ocd-campaign-finance-committee-type/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', regex='^ocd-campaign-finance-committee-type/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$')])),
                ('name', models.CharField(help_text='Name of the Committee Type.', max_length=100)),
                ('jurisdiction', models.ForeignKey(help_text='Reference to the Jurisdiction which defines the Committee Type.', on_delete=django.db.models.deletion.PROTECT, related_name='campaign_finance_committee_types', to='core.Jurisdiction')),
            ],
            options={
                'db_table': 'opencivicdata_committeetype',
            },
        ),
        migrations.CreateModel(
            name='Filing',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='The date and time of creation.')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='The date and time of the last update.')),
                ('extras', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, help_text='A key-value store for storing arbitrary information not covered elsewhere.')),
                ('locked_fields', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, default=list, size=None)),
                ('id', opencivicdata.core.models.base.OCDIDField(ocd_type='campaign-finance-filing', serialize=False, validators=[django.core.validators.RegexValidator(flags=32, message='ID must match ^ocd-campaign-finance-filing/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', regex='^ocd-campaign-finance-filing/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$')])),
                ('classification', models.CharField(blank=True, help_text='The type of filing, as defined by the jurisdiction in which it was filed.', max_length=100)),
                ('coverage_start_date', models.DateField(blank=True, help_text='Date when filing period of coverage begins.')),
                ('coverage_end_date', models.DateField(blank=True, help_text='Date when filing period of coverage ends.')),
                ('filer', models.ForeignKey(help_text='Reference to the Committee making the Filing.', on_delete=django.db.models.deletion.PROTECT, related_name='filings', to='campaign_finance.Committee')),
                ('recipient', models.ForeignKey(help_text='Reference to the Organization that is the regulator to which the filing was submitted.', on_delete=django.db.models.deletion.PROTECT, related_name='filings_received', to='core.Organization')),
            ],
            options={
                'db_table': 'opencivicdata_filing',
            },
        ),
        migrations.CreateModel(
            name='FilingAction',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='The date and time of creation.')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='The date and time of the last update.')),
                ('extras', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, help_text='A key-value store for storing arbitrary information not covered elsewhere.')),
                ('locked_fields', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, default=list, size=None)),
                ('id', opencivicdata.core.models.base.OCDIDField(ocd_type='campaign-finance-filing-action', serialize=False, validators=[django.core.validators.RegexValidator(flags=32, message='ID must match ^ocd-campaign-finance-filing-action/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', regex='^ocd-campaign-finance-filing-action/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$')])),
                ('classification', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100), help_text='Classification for the action, such as "amendment" or "revocation".', size=None)),
                ('description', models.CharField(help_text='Description of the action.', max_length=100)),
                ('date', models.DateField(help_text='The date the action occurred')),
                ('supersedes_prior_versions', models.BooleanField(default=False, help_text='Indicates whether this action renders everything contained in previous versions of this Filing invalid.')),
                ('is_current', models.BooleanField(default=True, help_text='Indicates whether data from this action (primarily the transaction list) should be considered current.')),
                ('agent', models.ManyToManyField(db_table='opencivicdata_filingactionagent', help_text='Person responsible for the action, usually the filer of the amendment or withdrawal.', related_name='filing_actions', to='core.Person')),
                ('filing', models.ForeignKey(help_text='Reference to the Filing in which the action was reported.', on_delete=django.db.models.deletion.CASCADE, related_name='actions', to='campaign_finance.Filing')),
            ],
            options={
                'db_table': 'opencivicdata_filingaction',
            },
        ),
        migrations.CreateModel(
            name='FilingActionSummaryAmount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(help_text='Description of the total (e.g., "Unitemized contributions" or "Total expenditures").', max_length=100)),
                ('amount_value', models.FloatField(help_text='Decimal amount of transaction.')),
                ('amount_currency', models.CharField(help_text='Currency denomination of transaction.', max_length=3)),
                ('filing_action', models.ForeignKey(help_text='Reference to a FilingAction in which the summary amount was reported.', on_delete=django.db.models.deletion.CASCADE, related_name='summary_amounts', to='campaign_finance.FilingAction')),
            ],
            options={
                'db_table': 'opencivicdata_filingactionsummaryamount',
            },
        ),
        migrations.CreateModel(
            name='FilingIdentifier',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('identifier', models.CharField(help_text='A unique identifier developed by an upstream or third party source.', max_length=300)),
                ('scheme', models.CharField(help_text='The name of the service that created the identifier.', max_length=300)),
                ('filing', models.ForeignKey(help_text='Reference to the Filing identified by this alternative identifier.', on_delete=django.db.models.deletion.CASCADE, related_name='identifiers', to='campaign_finance.Filing')),
            ],
            options={
                'db_table': 'opencivicdata_filingidentifier',
            },
        ),
        migrations.CreateModel(
            name='FilingSource',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('note', models.CharField(blank=True, help_text='A short, optional note related to an object.', max_length=300)),
                ('url', models.URLField(help_text='A hyperlink related to an object.', max_length=2000)),
                ('filing', models.ForeignKey(help_text='Reference to the Filing this source verifies.', on_delete=django.db.models.deletion.CASCADE, related_name='sources', to='campaign_finance.Filing')),
            ],
            options={
                'db_table': 'opencivicdata_filingsource',
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='The date and time of creation.')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='The date and time of the last update.')),
                ('extras', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, help_text='A key-value store for storing arbitrary information not covered elsewhere.')),
                ('locked_fields', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, default=list, size=None)),
                ('id', opencivicdata.core.models.base.OCDIDField(ocd_type='campaign-finance-filing-transaction', serialize=False, validators=[django.core.validators.RegexValidator(flags=32, message='ID must match ^ocd-campaign-finance-filing-transaction/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', regex='^ocd-campaign-finance-filing-transaction/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$')])),
                ('classification', models.CharField(help_text='Type of transaction - contribution, expenditure, loan, transfer, other receipt, etc.', max_length=100)),
                ('amount_value', models.DecimalField(decimal_places=2, help_text='Decimal amount of transaction.', max_digits=14)),
                ('amount_currency', models.CharField(help_text='Currency denomination of transaction.', max_length=3)),
                ('is_in_kind', models.BooleanField(default=False, help_text='Indicates this is an in-kind (i.e., non-monetary) Transaction.')),
                ('sender_entity_type', models.CharField(choices=[('committee', 'Committee'), ('organization', 'Organization'), ('person', 'Person')], help_text='Type of entity of sender (e.g., "Person", "Organization", "Committee").', max_length=50)),
                ('recipient_entity_type', models.CharField(choices=[('committee', 'Committee'), ('organization', 'Organization'), ('person', 'Person')], help_text='Type of entity of recipient (e.g., "Person", "Organization", "Committee").', max_length=50)),
                ('date', models.DateField(help_text='Date reported for transaction.')),
                ('election', models.ForeignKey(help_text='Reference to the Election to which the transaction is designated.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='elections.Election')),
                ('filing_action', models.ForeignKey(help_text='Reference to the FilingAction in which the Transaction is reported.', on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='campaign_finance.FilingAction')),
                ('recipient_committee', models.ForeignKey(help_text='Reference to Committee that received the transaction, if recipient_entity_type is "Committee".', on_delete=django.db.models.deletion.PROTECT, related_name='transactions_received', to='campaign_finance.Committee')),
                ('recipient_organization', models.ForeignKey(help_text='Reference to Organization that received the transaction, if recipient_entity_type is "Organization".', on_delete=django.db.models.deletion.PROTECT, related_name='transactions_received', to='core.Organization')),
                ('recipient_person', models.ForeignKey(help_text='Reference to Person that sent the transaction, if recipient_entity_type is "Person".', on_delete=django.db.models.deletion.PROTECT, related_name='transactions_received', to='core.Person')),
                ('sender_committee', models.ForeignKey(help_text='Reference to Committee that sent the transaction, if sender_entity_type is "Committee".', on_delete=django.db.models.deletion.PROTECT, related_name='transactions_sent', to='campaign_finance.Committee')),
                ('sender_organization', models.ForeignKey(help_text='Reference to Organization that sent the transaction, if sender_entity_type is "Organization".', on_delete=django.db.models.deletion.PROTECT, related_name='transactions_sent', to='core.Organization')),
                ('sender_person', models.ForeignKey(help_text='Reference to Person that sent the transaction, if sender_entity_type is "Person".', on_delete=django.db.models.deletion.PROTECT, related_name='transactions_sent', to='core.Person')),
            ],
            options={
                'db_table': 'opencivicdata_transaction',
            },
        ),
        migrations.CreateModel(
            name='TransactionIdentifier',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('identifier', models.CharField(help_text='A unique identifier developed by an upstream or third party source.', max_length=300)),
                ('scheme', models.CharField(help_text='The name of the service that created the identifier.', max_length=300)),
                ('transaction', models.ForeignKey(help_text='Reference to the Transaction identified by this alternative identifier.', on_delete=django.db.models.deletion.CASCADE, related_name='identifiers', to='campaign_finance.Transaction')),
            ],
            options={
                'db_table': 'opencivicdata_transactionidentifier',
            },
        ),
        migrations.CreateModel(
            name='TransactionNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField(help_text='Text of the note.')),
                ('transaction', models.ForeignKey(help_text='Reference to a Transaction described by the note.', on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='campaign_finance.Transaction')),
            ],
            options={
                'db_table': 'opencivicdata_transactionnote',
            },
        ),
        migrations.CreateModel(
            name='TransactionSource',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('note', models.CharField(blank=True, help_text='A short, optional note related to an object.', max_length=300)),
                ('url', models.URLField(help_text='A hyperlink related to an object.', max_length=2000)),
                ('transaction', models.ForeignKey(help_text='Reference to the Transaction this source verifies.', on_delete=django.db.models.deletion.CASCADE, related_name='sources', to='campaign_finance.Transaction')),
            ],
            options={
                'db_table': 'opencivicdata_transactionsource',
            },
        ),
        migrations.AddField(
            model_name='committee',
            name='committee_type',
            field=models.ForeignKey(help_text="Reference to the Committee's type, as defined by its Jurisdiction.", on_delete=django.db.models.deletion.PROTECT, related_name='committees', to='campaign_finance.CommitteeType'),
        ),
        migrations.AddField(
            model_name='committee',
            name='parent',
            field=models.ForeignKey(help_text="A link to another Committee that serves as this Committee's parent.", null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='campaign_finance.Committee'),
        ),
    ]

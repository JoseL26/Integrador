# Generated by Django 3.1.6 on 2021-04-03 01:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movil', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CaterogiaEquipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Desc_categoria', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cod_equipo', models.CharField(max_length=10, unique=True)),
                ('Desc_equipo', models.CharField(max_length=50)),
                ('Modelo', models.CharField(max_length=30)),
                ('Modelo_motor', models.CharField(max_length=30)),
                ('Estado', models.IntegerField()),
                ('CaterogiaEq', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movil.caterogiaequipo')),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Desc_marca', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterModelOptions(
            name='cargo',
            options={'ordering': ['Descripcion']},
        ),
        migrations.AlterModelOptions(
            name='categoria',
            options={'ordering': ['Descripcion'], 'verbose_name_plural': 'Categorias'},
        ),
        migrations.AlterModelOptions(
            name='empleado',
            options={'ordering': ['Apellidos']},
        ),
        migrations.AlterField(
            model_name='cargo',
            name='Estado',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='Estado',
            field=models.IntegerField(),
        ),
        migrations.CreateModel(
            name='ParteHoras',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('Empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movil.empleado')),
            ],
        ),
        migrations.CreateModel(
            name='OrdenTrabajo',
            fields=[
                ('Orden', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('eq_sistema', models.CharField(max_length=10)),
                ('conjunto', models.CharField(max_length=5)),
                ('desc_conjunto', models.CharField(max_length=30)),
                ('fase', models.CharField(max_length=4)),
                ('Responsable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movil.empleado')),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movil.equipo')),
            ],
        ),
        migrations.CreateModel(
            name='Operciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Descripcion', models.CharField(max_length=50)),
                ('Etapa', models.CharField(max_length=10)),
                ('Resposable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movil.empleado')),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movil.equipo')),
                ('orden', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movil.ordentrabajo')),
            ],
        ),
        migrations.AddField(
            model_name='equipo',
            name='Marca',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movil.marca'),
        ),
        migrations.CreateModel(
            name='DetalleParte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NumParte', models.ManyToManyField(to='movil.ParteHoras')),
                ('Orden', models.ManyToManyField(to='movil.OrdenTrabajo')),
                ('operacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movil.operciones')),
            ],
        ),
    ]

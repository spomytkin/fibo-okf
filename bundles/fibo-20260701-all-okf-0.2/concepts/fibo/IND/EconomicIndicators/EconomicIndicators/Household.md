---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: household
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: individual or small group of persons who occupy a housing unit (such as a house or apartment) as their usual place
      of residence, who pool some, or all, of their income and wealth and who consume certain types of goods and services
      collectively, mainly housing and food
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: 'A household may be either (a) a one-person household, that is to say, a person who makes provision for his or
      her own food or other essentials for living without combining with any other person to form part of a multi-person household
      or (b) a multi-person household, that is to say, a group of two or more persons living together who make common provision
      for food or other essentials for living. The persons in the group may pool their incomes and may, to a greater or lesser
      extent, have a common budget; they may be related or unrelated persons or constitute a combination of persons both related
      and unrelated.


      A household may be located in a housing unit or in a set of collective living quarters such as a boarding house, a hotel
      or a camp, or may comprise the administrative personnel in an institution. The household may also be homeless.'
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: From the perspective of the U.S Census Bureau, a household includes the related family members and all the unrelated
      people, if any, such as lodgers, foster children, wards, or employees who share the housing unit. A person living alone
      in a housing unit, or a group of unrelated people sharing a housing unit such as partners or roomers, is also counted
      as a household. The count of households excludes group quarters [such as institutional facilities]. There are two major
      categories of households, 'family' and 'nonfamily'.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  related_to:
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    resource: http://stats.oecd.org/glossary/detail.asp?ID=1255
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/Person
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/hasMember
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/HousingUnit
    kind: max_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Locations/hasLocation
  subclass_of:
  - concept: /concepts/fibo/IND/EconomicIndicators/EconomicIndicators/InstitutionalUnit.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/InstitutionalUnit
resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/Household
sources:
- id: fibo-source-8403bfa401
  resource: references/fibo/IND/EconomicIndicators/EconomicIndicators.rdf
  sha256: 8403bfa40177c207d84c314ab9dc8e157b1928c8ac8b2d5ba84d9260106576c5
  title: FIBO source IND/EconomicIndicators/EconomicIndicators.rdf
title: household
type: Ontology Class
---

# household

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/Household>

## Definition

individual or small group of persons who occupy a housing unit (such as a house or apartment) as their usual place of residence, who pool some, or all, of their income and wealth and who consume certain types of goods and services collectively, mainly housing and food

## Relationships

- **Related to**: [detail.asp](<http://stats.oecd.org/glossary/detail.asp?ID=1255>)
- **Subclass of**: [InstitutionalUnit](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/InstitutionalUnit.md)

## Constraints

- **[hasMember](<https://www.omg.org/spec/Commons/Collections/hasMember>)**: some values from of type [Person](/concepts/fibo/FND/AgentsAndPeople/People/Person.md)
- **[hasLocation](<https://www.omg.org/spec/Commons/Locations/hasLocation>)**: max qualified cardinality 1 of type [HousingUnit](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/HousingUnit.md)

## Annotations

- **label**: household
- **definition**: individual or small group of persons who occupy a housing unit (such as a house or apartment) as their usual place of residence, who pool some, or all, of their income and wealth and who consume certain types of goods and services collectively, mainly housing and food
- **explanatoryNote**: A household may be either (a) a one-person household, that is to say, a person who makes provision for his or her own food or other essentials for living without combining with any other person to form part of a multi-person household or (b) a multi-person household, that is to say, a group of two or more persons living together who make common provision for food or other essentials for living. The persons in the group may pool their incomes and may, to a greater or lesser extent, have a common budget; they may be related or unrelated persons or constitute a combination of persons both related and unrelated.  A household may be located in a housing unit or in a set of collective living quarters such as a boarding house, a hotel or a camp, or may comprise the administrative personnel in an institution. The household may also be homeless.
- **explanatoryNote**: From the perspective of the U.S Census Bureau, a household includes the related family members and all the unrelated people, if any, such as lodgers, foster children, wards, or employees who share the housing unit. A person living alone in a housing unit, or a group of unrelated people sharing a housing unit such as partners or roomers, is also counted as a household. The count of households excludes group quarters [such as institutional facilities]. There are two major categories of households, 'family' and 'nonfamily'.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: North American Industry Classification System scheme
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: the scheme defining the North American Industry Classification System (NAICS) Codes
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: 'The North American Industry Classification System (NAICS) is the standard used by Federal statistical agencies
      in classifying business establishments for the purpose of collecting, analyzing, and publishing statistical data related
      to the U.S. business economy.


      NAICS was developed under the auspices of the Office of Management and Budget (OMB), and adopted in 1997 to replace
      the Standard Industrial Classification (SIC) system. It was developed jointly by the U.S. Economic Classification Policy
      Committee (ECPC), Statistics Canada and Mexico''s Instituto Nacional Estadistica y Geografia, to allow for a high level
      of comparability in business statistics among the North American countries.'
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/NorthAmericanIndustryClassificationSystemCode
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Designators/defines
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: https://www.census.gov/naics/
  subclass_of:
  - concept: /concepts/fibo/FND/Arrangements/ClassificationSchemes/IndustrySectorClassificationScheme.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/ClassificationSchemes/IndustrySectorClassificationScheme
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/CodesAndCodeSets/CodeSet
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/NorthAmericanIndustryClassificationSystemScheme
sources:
- id: fibo-source-fdadb56cd3
  resource: references/fibo/FBC/FunctionalEntities/BusinessRegistries.rdf
  sha256: fdadb56cd346c7f354007b53bb21e21e35b8d83160f45c626d0f675b7b14754d
  title: FIBO source FBC/FunctionalEntities/BusinessRegistries.rdf
title: North American Industry Classification System scheme
type: Ontology Class
---

# North American Industry Classification System scheme

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/NorthAmericanIndustryClassificationSystemScheme>

## Definition

the scheme defining the North American Industry Classification System (NAICS) Codes

## Relationships

- **See also**: [naics](<https://www.census.gov/naics/>)
- **Subclass of**: [IndustrySectorClassificationScheme](/concepts/fibo/FND/Arrangements/ClassificationSchemes/IndustrySectorClassificationScheme.md)
- **Subclass of**: [CodeSet](<https://www.omg.org/spec/Commons/CodesAndCodeSets/CodeSet>)

## Constraints

- **[defines](<https://www.omg.org/spec/Commons/Designators/defines>)**: some values from of type [NorthAmericanIndustryClassificationSystemCode](/concepts/fibo/FBC/FunctionalEntities/BusinessRegistries/NorthAmericanIndustryClassificationSystemCode.md)

## Annotations

- **label**: North American Industry Classification System scheme
- **definition**: the scheme defining the North American Industry Classification System (NAICS) Codes
- **explanatoryNote**: The North American Industry Classification System (NAICS) is the standard used by Federal statistical agencies in classifying business establishments for the purpose of collecting, analyzing, and publishing statistical data related to the U.S. business economy.  NAICS was developed under the auspices of the Office of Management and Budget (OMB), and adopted in 1997 to replace the Standard Industrial Classification (SIC) system. It was developed jointly by the U.S. Economic Classification Policy Committee (ECPC), Statistics Canada and Mexico's Instituto Nacional Estadistica y Geografia, to allow for a high level of comparability in business statistics among the North American countries.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

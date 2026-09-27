---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: standard industrial classification scheme
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: the scheme defining the Standard Industrial Classification (SIC) Code List
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Standard Industrial Classifications are four-digit codes that categorize companies by the type of business activities
      they engage in. These codes were created by the U.S. government in 1937 to facilitate analysis of economic activity
      across government agencies and within industries. They were mostly replaced in 1997 by a new system of six-digit codes
      called the North American Industry Classification System (NAICS). The new codes were adopted in part to standardize
      industry data collection and analysis in between Canada, the United States and Mexico which had entered into the North
      American Free Trade Agreement. Note that certain organizations, such as the Securities and Exchange Commission (SEC)
      still use SIC codes for some purposes.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/StandardIndustrialClassificationCode
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Designators/defines
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: https://www.osha.gov/pls/imis/sic_manual.html/
  subclass_of:
  - concept: /concepts/fibo/FND/Arrangements/ClassificationSchemes/IndustrySectorClassificationScheme.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/ClassificationSchemes/IndustrySectorClassificationScheme
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/CodesAndCodeSets/CodeSet
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/StandardIndustrialClassificationScheme
sources:
- id: fibo-source-fdadb56cd3
  resource: references/fibo/FBC/FunctionalEntities/BusinessRegistries.rdf
  sha256: fdadb56cd346c7f354007b53bb21e21e35b8d83160f45c626d0f675b7b14754d
  title: FIBO source FBC/FunctionalEntities/BusinessRegistries.rdf
title: standard industrial classification scheme
type: Ontology Class
---

# standard industrial classification scheme

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/StandardIndustrialClassificationScheme>

## Definition

the scheme defining the Standard Industrial Classification (SIC) Code List

## Relationships

- **See also**: [sic_manual.html](<https://www.osha.gov/pls/imis/sic_manual.html/>)
- **Subclass of**: [IndustrySectorClassificationScheme](/concepts/fibo/FND/Arrangements/ClassificationSchemes/IndustrySectorClassificationScheme.md)
- **Subclass of**: [CodeSet](<https://www.omg.org/spec/Commons/CodesAndCodeSets/CodeSet>)

## Constraints

- **[defines](<https://www.omg.org/spec/Commons/Designators/defines>)**: some values from of type [StandardIndustrialClassificationCode](/concepts/fibo/FBC/FunctionalEntities/BusinessRegistries/StandardIndustrialClassificationCode.md)

## Annotations

- **label**: standard industrial classification scheme
- **definition**: the scheme defining the Standard Industrial Classification (SIC) Code List
- **explanatoryNote**: Standard Industrial Classifications are four-digit codes that categorize companies by the type of business activities they engage in. These codes were created by the U.S. government in 1937 to facilitate analysis of economic activity across government agencies and within industries. They were mostly replaced in 1997 by a new system of six-digit codes called the North American Industry Classification System (NAICS). The new codes were adopted in part to standardize industry data collection and analysis in between Canada, the United States and Mexico which had entered into the North American Free Trade Agreement. Note that certain organizations, such as the Securities and Exchange Commission (SEC) still use SIC codes for some purposes.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

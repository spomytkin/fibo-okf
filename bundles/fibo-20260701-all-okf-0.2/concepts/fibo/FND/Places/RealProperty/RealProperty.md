---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: real property
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: physical asset defined as land together with any structures that are permanently attached to that land, such as
      houses, trees, fences and improvements
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.law.cornell.edu/cfr/text/10/600.101
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Real property may be classified according to its general use as residential, commercial, agricultural, industrial,
      or special purpose. This term is sometimes used synonymously with 'real estate', though not in all circumstances under
      US law.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Real property typically encompasses both the physical land and everything that lies above, below, or on its surface,
      including any fixed structures, natural resources, and rights or interests (e.g., mineral rights). There are cases,
      such as condominiums, in which the interior of the structure is owned by a party that may not own the land. There are
      also cases in which certain long-term leases have similar characteristics to ownership, but are time-bound.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: parcel
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Places/RealProperty/RealPropertyAppraisal
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isEvaluatedBy
  - filler: http://www.w3.org/2001/XMLSchema#positiveInteger
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/MortgageOrigination/hasNumberOfAffordableDwellingUnits
  - filler: http://www.w3.org/2001/XMLSchema#positiveInteger
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/MortgageOrigination/hasNumberOfDwellingUnits
  - filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/MortgageOrigination/DwellingCapacity
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
  - filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/MortgageOrigination/ManufacturedHomeLegalClassification
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: https://www.investopedia.com/terms/r/real-property.asp
  subclass_of:
  - concept: /concepts/fibo/FND/OwnershipAndControl/Ownership/PhysicalAsset.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/PhysicalAsset
  - concept: /concepts/fibo/FND/Places/RealProperty/RealEstate.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/RealProperty/RealEstate
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/RealProperty/RealProperty
sources:
- id: fibo-source-f0e5ecd06c
  resource: references/fibo/FND/Places/RealProperty.rdf
  sha256: f0e5ecd06c164d1e5fff0c1236869b2014bcba3d7008365dcc2c7363064202bd
  title: FIBO source FND/Places/RealProperty.rdf
- id: fibo-source-939ceaa7d7
  resource: references/fibo/LOAN/RealEstateLoans/MortgageOrigination.rdf
  sha256: 939ceaa7d7758108e99a4653c0d982fdf5cb9bce32f07927542f3b01508e593a
  title: FIBO source LOAN/RealEstateLoans/MortgageOrigination.rdf
title: real property
type: Ontology Class
---

# real property

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Places/RealProperty/RealProperty>

## Definition

physical asset defined as land together with any structures that are permanently attached to that land, such as houses, trees, fences and improvements

## Relationships

- **See also**: [real-property.asp](<https://www.investopedia.com/terms/r/real-property.asp>)
- **Subclass of**: [PhysicalAsset](/concepts/fibo/FND/OwnershipAndControl/Ownership/PhysicalAsset.md)
- **Subclass of**: [RealEstate](/concepts/fibo/FND/Places/RealProperty/RealEstate.md)

## Constraints

- **[isEvaluatedBy](/concepts/fibo/FND/Relations/Relations/isEvaluatedBy.md)**: min qualified cardinality 0 of type [RealPropertyAppraisal](/concepts/fibo/FND/Places/RealProperty/RealPropertyAppraisal.md)
- **[hasNumberOfAffordableDwellingUnits](/concepts/fibo/LOAN/RealEstateLoans/MortgageOrigination/hasNumberOfAffordableDwellingUnits.md)**: some values from of type [positiveInteger](<http://www.w3.org/2001/XMLSchema#positiveInteger>)
- **[hasNumberOfDwellingUnits](/concepts/fibo/LOAN/RealEstateLoans/MortgageOrigination/hasNumberOfDwellingUnits.md)**: some values from of type [positiveInteger](<http://www.w3.org/2001/XMLSchema#positiveInteger>)
- **[isClassifiedBy](<https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy>)**: some values from of type [DwellingCapacity](/concepts/fibo/LOAN/RealEstateLoans/MortgageOrigination/DwellingCapacity.md)
- **[isClassifiedBy](<https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy>)**: some values from of type [ManufacturedHomeLegalClassification](/concepts/fibo/LOAN/RealEstateLoans/MortgageOrigination/ManufacturedHomeLegalClassification.md)

## Annotations

- **label** (en): real property
- **definition** (en): physical asset defined as land together with any structures that are permanently attached to that land, such as houses, trees, fences and improvements
- **adaptedFrom**: https://www.law.cornell.edu/cfr/text/10/600.101
- **explanatoryNote** (en): Real property may be classified according to its general use as residential, commercial, agricultural, industrial, or special purpose. This term is sometimes used synonymously with 'real estate', though not in all circumstances under US law.
- **explanatoryNote** (en): Real property typically encompasses both the physical land and everything that lies above, below, or on its surface, including any fixed structures, natural resources, and rights or interests (e.g., mineral rights). There are cases, such as condominiums, in which the interior of the structure is owned by a party that may not own the land. There are also cases in which certain long-term leases have similar characteristics to ownership, but are time-bound.
- **synonym** (en): parcel

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

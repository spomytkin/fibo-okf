---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: charge category
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Examples include closing costs, interest, taxes, and other service-related fees.
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: classifier indicating what a particular fee or other expense is for
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/usageNote
    value: Use with LineItem, (has ChargeCategory instance), (hasNumericalValue for number of units) and (hasCost for the
      amount of money)
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Classifiers/Classifier
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/MortgageOrigination/ChargeCategory
sources:
- id: fibo-source-939ceaa7d7
  resource: references/fibo/LOAN/RealEstateLoans/MortgageOrigination.rdf
  sha256: 939ceaa7d7758108e99a4653c0d982fdf5cb9bce32f07927542f3b01508e593a
  title: FIBO source LOAN/RealEstateLoans/MortgageOrigination.rdf
title: charge category
type: Ontology Class
---

# charge category

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/MortgageOrigination/ChargeCategory>

## Definition

classifier indicating what a particular fee or other expense is for

## Additional definitions

- Examples include closing costs, interest, taxes, and other service-related fees.

## Relationships

- **Subclass of**: [Classifier](<https://www.omg.org/spec/Commons/Classifiers/Classifier>)

## Annotations

- **label**: charge category
- **definition**: Examples include closing costs, interest, taxes, and other service-related fees.
- **definition**: classifier indicating what a particular fee or other expense is for
- **usageNote**: Use with LineItem, (has ChargeCategory instance), (hasNumericalValue for number of units) and (hasCost for the amount of money)

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

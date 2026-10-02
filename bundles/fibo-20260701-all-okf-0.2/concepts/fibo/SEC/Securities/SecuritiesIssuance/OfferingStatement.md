---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: offering statement
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: offering memorandum that conforms to Regulation A, Offering Statement, of the Securities Act of 1933
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: See https://www.sec.gov/about/forms/form1-a.pdf for the actual form detail
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/SEC/Securities/SecuritiesIssuance/OfferingDocument.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/OfferingDocument
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/OfferingStatement
sources:
- id: fibo-source-7b3088e831
  resource: references/fibo/SEC/Securities/SecuritiesIssuance.rdf
  sha256: 7b3088e8315beedb43222e345522bb546f87fbbd6850833103c9ba84ea1d7ac0
  title: FIBO source SEC/Securities/SecuritiesIssuance.rdf
title: offering statement
type: Ontology Class
---

# offering statement

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/OfferingStatement>

## Definition

offering memorandum that conforms to Regulation A, Offering Statement, of the Securities Act of 1933

## Relationships

- **Subclass of**: [OfferingDocument](/concepts/fibo/SEC/Securities/SecuritiesIssuance/OfferingDocument.md)

## Annotations

- **label**: offering statement
- **definition**: offering memorandum that conforms to Regulation A, Offering Statement, of the Securities Act of 1933
- **explanatoryNote**: See https://www.sec.gov/about/forms/form1-a.pdf for the actual form detail

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: private placement memorandum
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: legal document stating the objectives, risks and terms of investment involved with a private placement
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: PPM
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: Barron's Dictionary of Finance and Investment Terms, Ninth Edition, 2014.
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: http://www.investopedia.com/terms/o/offeringmemorandum.asp
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: An offering memorandum serves to provide buyers with information on the offering and to protect the sellers from
      the liability associated with selling unregistered securities. It includes information such as the financial statements,
      management biographies, a detailed description of the business, etc.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: offering memorandum
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/SEC/Securities/SecuritiesIssuance/OfferingDocument.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/OfferingDocument
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/PrivatePlacementMemorandum
sources:
- id: fibo-source-7b3088e831
  resource: references/fibo/SEC/Securities/SecuritiesIssuance.rdf
  sha256: 7b3088e8315beedb43222e345522bb546f87fbbd6850833103c9ba84ea1d7ac0
  title: FIBO source SEC/Securities/SecuritiesIssuance.rdf
title: private placement memorandum
type: Ontology Class
---

# private placement memorandum

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/PrivatePlacementMemorandum>

## Definition

legal document stating the objectives, risks and terms of investment involved with a private placement

## Relationships

- **Subclass of**: [OfferingDocument](/concepts/fibo/SEC/Securities/SecuritiesIssuance/OfferingDocument.md)

## Annotations

- **label**: private placement memorandum
- **definition**: legal document stating the objectives, risks and terms of investment involved with a private placement
- **abbreviation**: PPM
- **adaptedFrom**: Barron's Dictionary of Finance and Investment Terms, Ninth Edition, 2014.
- **adaptedFrom**: http://www.investopedia.com/terms/o/offeringmemorandum.asp
- **explanatoryNote**: An offering memorandum serves to provide buyers with information on the offering and to protect the sellers from the liability associated with selling unregistered securities. It includes information such as the financial statements, management biographies, a detailed description of the business, etc.
- **synonym**: offering memorandum

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

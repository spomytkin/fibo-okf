---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: real estate
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: real property, interests in mortgages on real property (including interests in mortgages on leaseholds of land
      or improvements thereon), and shares in qualified real estate investment trusts
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.law.cornell.edu/cfr/text/26/1.856-3
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The term 'mortgages on real property' includes deeds of trust on real property. Note that interpretation of the
      term 'real estate' is context-dependent - this broader interpretation is used in tax law in the US and elsewhere.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: real estate asset
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/OwnershipAndControl/Ownership/Asset.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/Asset
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/RealProperty/RealEstate
sources:
- id: fibo-source-f0e5ecd06c
  resource: references/fibo/FND/Places/RealProperty.rdf
  sha256: f0e5ecd06c164d1e5fff0c1236869b2014bcba3d7008365dcc2c7363064202bd
  title: FIBO source FND/Places/RealProperty.rdf
title: real estate
type: Ontology Class
---

# real estate

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Places/RealProperty/RealEstate>

## Definition

real property, interests in mortgages on real property (including interests in mortgages on leaseholds of land or improvements thereon), and shares in qualified real estate investment trusts

## Relationships

- **Subclass of**: [Asset](/concepts/fibo/FND/OwnershipAndControl/Ownership/Asset.md)

## Annotations

- **label** (en): real estate
- **definition** (en): real property, interests in mortgages on real property (including interests in mortgages on leaseholds of land or improvements thereon), and shares in qualified real estate investment trusts
- **adaptedFrom**: https://www.law.cornell.edu/cfr/text/26/1.856-3
- **explanatoryNote** (en): The term 'mortgages on real property' includes deeds of trust on real property. Note that interpretation of the term 'real estate' is context-dependent - this broader interpretation is used in tax law in the US and elsewhere.
- **synonym** (en): real estate asset

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
